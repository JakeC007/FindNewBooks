"""
April 26, 2020
Author Jake Chanenson
This file is where I create functions to work around the broken parts of the goodreads wrapper.
"""

import requests
import xmltodict
import time
import book

"""
Creates a list of user's books taken from their shelves. The user must have their profile public
@param key - the api key
@param id - the account you want to search
@param shelf - the shelf to search
@return: Lst of book titles
"""

def list_user_book_t(key, id = 1, shelf='all'):
    return search_user_book_t(key, id, shelf)


"""
Searches a given shelf for a given term. The user must have their profile public
@param key - the api key
@param id - the account you want to search
@param shelf - the shelf to search
@param search - the string you want to search
@return: Lst of book titles that match the search
"""
def search_user_book_t(key, id = 1, shelf='all', search = None):
    retLst = []
    apiParams = {'key': key, 'shelf': shelf, 'id': id, 'per_page' : 50, 'page': 1, 'search[query]' : search}
    #Request to get total number of books, and how many are in the first page
    r = requests.get("https://www.goodreads.com/review/list?v=2", params=apiParams)
    data_dict = xmltodict.parse(r.content)
    amtAppended = 0
    total = int(data_dict['GoodreadsResponse']['reviews']['@total'])
    #read in the books from goodreads
    while(amtAppended!=total):
        r = requests.get("https://www.goodreads.com/review/list?v=2", params=apiParams)
        data_dict = xmltodict.parse(r.content)
        start =int(data_dict['GoodreadsResponse']['reviews']['@start'])
        amtAppended = int(data_dict['GoodreadsResponse']['reviews']['@end'])
        end = amtAppended-start+1
        for i in range(start-start,end):
            retLst.append(data_dict['GoodreadsResponse']['reviews']['review'][i]['book']['title'])
        time.sleep(1.2) #needed as to not violate Goodreads TOS
        apiParams['page']+=1 #move to next page

    return retLst

"""
Function finds a list of authors from a given user's shelf
@param key - the api key
@param id - the account you want to search
@param shelf - the shelf to search
@returns a list of authors and a list of author IDs from a given user's shelf
"""
def list_user_authors(key, id = 1, shelf='all'):
        retLstName = []
        retLstID = []
        seenLst = set(retLstName)
        apiParams = {'key': key, 'shelf': shelf, 'id': id, 'per_page' : 50, 'page': 1}
        #Request to get total number of books, and how many are in the first page
        r = requests.get("https://www.goodreads.com/review/list?v=2", params=apiParams)
        data_dict = xmltodict.parse(r.content)
        amtAppended = 0
        total = int(data_dict['GoodreadsResponse']['reviews']['@total'])
        #read in the books from goodreads
        while(amtAppended!=total):
            r = requests.get("https://www.goodreads.com/review/list?v=2", params=apiParams)
            data_dict = xmltodict.parse(r.content)
            start =int(data_dict['GoodreadsResponse']['reviews']['@start'])
            amtAppended = int(data_dict['GoodreadsResponse']['reviews']['@end'])
            end = amtAppended-start+1
            for i in range(start-start,end):
                item = data_dict['GoodreadsResponse']['reviews']['review'][i]['book']['authors']['author']['name']
                if item not in seenLst: #ensure there are no duplicates. set() has O(1) look up
                    seenLst.add(item)
                    retLstName.append(item)
                    retLstID.append(int(data_dict['GoodreadsResponse']['reviews']['review'][i]['book']['authors']['author']['id']))
            time.sleep(1.2) #needed as to not violate Goodreads TOS
            apiParams['page']+=1 #move to next page

        return retLstName, retLstID
"""
Function searches Goodreads for a given search term and returns a list of orderdDicts. Each dict contains info about each book.
@param key - the api key
@param q - the query you want to search
@param search - the type of search you want to do (title, author, all)
@return a list of book objects
"""
def find_books(key, q, search = 'author'):
    retLst = []
    apiParams = {'key': key, 'q' : q, 'search[field]' : search, 'page' : 1}
    #Request to get total number of books, and how many are in the first page
    r = requests.get("https://www.goodreads.com/search/index.xml", params=apiParams)
    data_dict = xmltodict.parse(r.content)
    amtAppended = 0
    total = int(data_dict['GoodreadsResponse']['search']['total-results'])
    #read in the books from goodreads
    while(amtAppended!=total):
        r = requests.get("https://www.goodreads.com/search/index.xml", params=apiParams)
        data_dict = xmltodict.parse(r.content)
        start = int(data_dict['GoodreadsResponse']['search']['results-start'])
        amtAppended = int(data_dict['GoodreadsResponse']['search']['results-end'])
        end = amtAppended-start+1
        for i in range(start-start, end):
            try:
                year = int(data_dict['GoodreadsResponse']['search']['results']['work'][i]['original_publication_year']['#text'])
            except:
                continue #skip items that don't have a year
            tempBook = book.GRBook(data_dict['GoodreadsResponse']['search']['results']['work'][i])
            retLst.append(tempBook)

        time.sleep(1.2) #needed as to not violate Goodreads TOS
        print("Grabbing Books Page %d of %d" % (apiParams['page'], ((total/20)+1)))
        apiParams['page']+=1 #move to next page

    return retLst

"""
Function searches Goodreads for a given author IDs and returns a list of orderdDicts. Each dict contains info about each book.
@param key - the api key
@param q - the query you want to search
@param search - the type of search you want to do (title, author, all)
@return a list of book objects
"""
def list_author_books(key, authorID):
    retLst = []
    seenLst = set(retLst)
    apiParams = {'key': key, 'id' : authorID, 'page' : 1}
    #Request to get total number of books, and how many are in the first page
    r = requests.get("https://www.goodreads.com/author/list.xml", params=apiParams)
    data_dict = xmltodict.parse(r.content)
    amtAppended = 0
    numPerPage = int(data_dict['GoodreadsResponse']['author']['books']['@end']) - int(data_dict['GoodreadsResponse']['author']['books']['@start'])
    total = int(data_dict['GoodreadsResponse']['author']['books']['@total'])

    #read in the books from goodreads
    while(amtAppended!=total):
        r = requests.get("https://www.goodreads.com/author/list.xml", params=apiParams)
        data_dict = xmltodict.parse(r.content)
        start = int(data_dict['GoodreadsResponse']['author']['books']['@start'])
        amtAppended = int(data_dict['GoodreadsResponse']['author']['books']['@end'])
        end = amtAppended-start+1
        print("Books Collected: %d" %(amtAppended))
        for i in range(start-start, end):
            try:
                year = int(data_dict['GoodreadsResponse']['author']['books']['book'][i]['publication_year'])
                title = data_dict['GoodreadsResponse']['author']['books']['book'][i]['title']
            except:
                continue #skip items that don't have a year
            if title not in seenLst: #prevent duplicate books 
                seenLst.add(title)
                tempBook = book.GR_Auth_Book(data_dict['GoodreadsResponse']['author']['books']['book'][i])
                retLst.append(tempBook)

        time.sleep(1.2) #needed as to not violate Goodreads TOS
        apiParams['page']+=1 #move to next page

    return retLst
