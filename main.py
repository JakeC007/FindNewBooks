#!/usr/bin/python3
"""
April 26, 2020
Author Jake Chanenson
"""

from secrets import key, secret, usrID
from goodreads import client
import miscFunc
import time
from datetime import date


def main():
    currentYear = date.today().year
    bookLst = []
    tempBookLst = []
    authorStr = ""
    authorLst = miscFunc.list_user_authors(key, usrID, 'authors-follow')
    print("Pulled Authors")
    print("Grabbing First Author's Books")
    #get each author's book list, and keep the books that were published within 2 years
    for author in authorLst:
        authorStr+= author+" "
         tempAuthorBooks = miscFunc.find_books(key, author)
         print("Pulled Next Author's Books")
         for book in tempAuthorBooks:
             if((book.publication_year() >=currentYear-2) and (book.publication_year() <= currentYear)):
                 tempBookLst.append(book)

    titlesUsrRead = miscFunc.list_user_book_t(key, usrID, 'read')
    for tb in tempBookLst:
        if(tb.title() in titlesUsrRead):
            bookLst.append(tb)

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
