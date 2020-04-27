#!/usr/bin/python3
"""
April 26, 2020
Author Jake Chanenson
"""

from secrets import key, secret
from goodreads import client
import time

def main():
    gc = client.GoodreadsClient(key, secret)
    authorLst = ["chambers", "doctorow", "scalzi", "James S.A.", "Butcher", ]
    bookLst = []
    for author in authorLst:
        a = gc.find_author(author)
        print(a.name)
        print(a.books)
        bookLst.append(a.books)
        print("----"*10)
        time.sleep(1)
    print(bookLst)

    # author = gc.find_author("chambers")
    # print(author.name)

    # time.sleep(1)
    # usr = gc.user(50914049)
    # print(usr.name)
    #author = gc.author(4763)
    #print(author.books)


if __name__ == "__main__":
    main()
