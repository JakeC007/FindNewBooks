#!/usr/bin/python3
"""
April 26, 2020
Author Jake Chanenson
"""

from secrets import key, secret, usrID
import miscFunc
from datetime import date


def main():
    currentYear = date.today().year
    bookLst = []
    tempBookLst = [] #cheaper to have a temp lst than use list remove--thats O(n)

    #get the list of authors that the user is interested in
    authorLst = miscFunc.list_user_authors(key, usrID, 'authors-follow')
    print("Pulled List Of Authors")
    print("Grabbing First Author's Books")

    #get list of each author's books, and keep the books that were published within 2 years
    for author in authorLst:
        print("Pulling Next Author's Books")
        tempAuthorBooks = miscFunc.find_books(key, author)
        for book in tempAuthorBooks:
            if((book.publication_year() >=currentYear-2) and (book.publication_year() <= currentYear)):
                tempBookLst.append(book)

    #grab the user's read shelf. Compare those titles to the titles in the list of author books and keep the unread
    titlesUsrRead = miscFunc.list_user_book_t(key, usrID, 'read')
    for tb in tempBookLst:
        if(tb.title() not in titlesUsrRead):
            bookLst.append(tb)

    #generate email body
    body = f"Hey, \n Some of your favorite authors have new books out that you haven't read: \n {unpack(bookLst)}"\
           f"\nRemember, these books come from the following authors {authors(authorLst)}. If you wish to change which authors to follow, "\
           f"please edit your shelf entitled 'authors-follow'. "
    print(body)


"""
Pretty string formatting for the books
@param books - list of book objects
@return formatted string of books in a list
"""
def unpack(books):
    retStr = ' '
    for book in books:
        tempStr = '\t*{0} by {1}\n'.format(book.title(), book.author_name())
        retStr+=tempStr
    return retStr

"""
Pretty string formatting for the authors
@param lst - list of author names
@return formatted string of authors
"""
def authors(lst):
    retStr = ''
    for i in range(len(lst)):
        if i != len(lst)-1:
            tempStr = '{0}, '.format(lst[i])
        else:
            tempStr = 'and {0}'.format(lst[i])
        retStr+=tempStr
    return retStr





    #remove untitled books from list

    #write email
        #author string
        #formatted lst













    """
    new plan use find_books func to collect a list of work obj from each of the authors
    use work.year to find the year and work.title to get the title
    """


    # gc = client.GoodreadsClient(key, secret)
    #
    # for author in authorLst:
    #     a = gc.find_author(author)
    #     print(a.name)
    #     print(a.books)
    #
    #
    #     #check to see wich books came out  within the last 18 months or so
    #     #see if those books are on my read list
    #     #if it passes both of those, add book to bookLst
    #
    #
    #
    #     bookLst.append(a.books)
    #     print("----"*10)
    #     time.sleep(1)
    # print(bookLst)



if __name__ == "__main__":
    main()
