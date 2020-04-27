"""
April 26, 2020
Author Jake Chanenson
This file is where I create functions to work around the broken parts of the goodreads wrapper.
"""

import requests
import xmltodict
import time

"""
Creates a list of user's books taken from their shelves. The user must have their profile public
@param key - the api key
@param id - the account you want to search
@param shelf - the shelf to search
@return: Lst of book titles
"""

def list_user_books(key, id = 1, shelf='all'):
    print("in func 1")
    return search_user_books(key, id, shelf)


"""
Searches a given shelf for a given term. The user must have their profile public
@param key - the api key
@param id - the account you want to search
@param shelf - the shelf to search
@param search - the string you want to search
@return: Lst of book titles that match the search
"""

def search_user_books(key, id = 1, shelf='all', search = None):
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

def list_user_authors(key, id = 1, shelf='all'):
        retLst = []
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
                retLst.append(data_dict['GoodreadsResponse']['reviews']['review'][i]['book']['authors']['author']['name'])
            time.sleep(1.2) #needed as to not violate Goodreads TOS
            apiParams['page']+=1 #move to next page

        return retLst

def find_books(key, q, search = 'author'):
    retLst = []
    apiParams = {'key': key, 'q' : q, 'search[field]' : search, 'page' : 1}
    #Request to get total number of books, and how many are in the first page
    r = requests.get("https://www.goodreads.com/search/index.xml", params=apiParams)
    data_dict = xmltodict.parse(r.content)
    print(r.url)
    start = int(data_dict['GoodreadsResponse']['search']['results-start'])
    end = int(data_dict['GoodreadsResponse']['search']['results-end'])
    for i in range(start-1, end):
        try:
            year = int(data_dict['GoodreadsResponse']['search']['results']['work'][i]['original_publication_year']['#text'])
        except:
            year = -1
        title = (data_dict['GoodreadsResponse']['search']['results']['work'][i]['best_book']['title'])
        print("%s, %d" % (title, year))

    # amtAppended = 0
    # total = int(data_dict['GoodreadsResponse']['reviews']['@total'])
    # #read in the books from goodreads
    # while(amtAppended!=total):
    #     r = requests.get("https://www.goodreads.com/search/index.xml", params=apiParams)
    #     data_dict = xmltodict.parse(r.content)
    #     start =int(data_dict['GoodreadsResponse']['reviews']['@start'])
    #     amtAppended = int(data_dict['GoodreadsResponse']['reviews']['@end'])
    #     end = amtAppended-start+1
    #     for i in range(start-start,end):
    #         retLst.append(data_dict['GoodreadsResponse']['reviews']['review'][i]['book']['authors']['author']['name'])
    #     time.sleep(1.2) #needed as to not violate Goodreads TOS
    #     apiParams['page']+=1 #move to next page

    return retLst
