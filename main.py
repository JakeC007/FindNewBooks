#!/usr/bin/python3
"""
April 26, 2020
Author Jake Chanenson
"""

from secrets import key, secret
from goodreads import client
import miscFunc
import time


def main():
    authorLst = miscFunc.list_user_authors(key, 50914049, 'authors-follow')
    bookLst = []
    # for author in authorLst:
    #     print(miscFunc.find_books(key, author))
    for author in authorLst:
        pval = miscFunc.find_books(key, author)
        for p in pval:
            print("%s Published %d,%d" %(p.title(), p.publication_month(), p.publication_year()))
        print(len(pval))

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
