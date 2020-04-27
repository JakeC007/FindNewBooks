#!/usr/bin/python3
"""
April 26, 2020
Author Jake Chanenson
"""

from secrets import key, secret
from goodreads import client
import time
import requests
import xmltodict

def main():

    #r = requests.get("https://www.goodreads.com/review/list50914049.xml?key=TWuS8AWNBQq0Jx4QxinwQ&v=2")
    #r=requests.get("https://www.goodreads.com/author/show/18541?format=xml&key=TWuS8AWNBQq0Jx4QxinwQ")
    bleh = {'key': key, 'shelf':'read', 'id': '50914049', 'per_page' : 50, 'page': 1}
    r=requests.get("https://www.goodreads.com/review/list?v=2", params=bleh)

    data_dict = xmltodict.parse(r.content)
    start = int(data_dict['GoodreadsResponse']['reviews']['@start'])
    end = int(data_dict['GoodreadsResponse']['reviews']['@end'])
    total = int(data_dict['GoodreadsResponse']['reviews']['@total'])

    for i in range(start-start,end-start):
        print(data_dict['GoodreadsResponse']['reviews']['review'][i]['book']['title'])

    while(end!=total):
        time.sleep(1.2)
        bleh['page']+=1
        r=requests.get("https://www.goodreads.com/review/list?v=2", params=bleh)
        data_dict = xmltodict.parse(r.content)
        start =int(data_dict['GoodreadsResponse']['reviews']['@start'])
        end = int(data_dict['GoodreadsResponse']['reviews']['@end'])

        for i in range(start-start,end-start):
            print(data_dict['GoodreadsResponse']['reviews']['review'][i]['book']['title'])









    #print(data_dict['GoodreadsResponse']['author']['name'])




    # gc = client.GoodreadsClient(key, secret)

    # usr = gc.user(50914049)
    # print(usr.name)
    # s = usr.shelves
    # print(usr.owned_books)
    # print(type(s))
    # print(type(usr.name))

    # p = gc.user(1)
    # print(p.name)
    # print(p.shelves)

    # authorLst = ["chambers", "doctorow", "scalzi", "James S.A.", "Butcher", ]
    # bookLst = []
    # for author in authorLst:
    #     a = gc.find_author(author)
    #     print(a.name)
    #     print(a.books)
    #     bookLst.append(a.books)
    #     print("----"*10)
    #     time.sleep(1)
    # print(bookLst)

    # author = gc.find_author("chambers")
    # print(author.name)

    # time.sleep(1)

    #author = gc.author(4763)
    #print(author.books)


if __name__ == "__main__":
    main()
