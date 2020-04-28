"""
April 27, 2020
This file contains a Goodreads book class
Unless noted in the return, the methods return strings.
"""

class GRBook:
    def __init__(self, book_dict):
        self.book_dict = book_dict

    def __repr__(self):
        return self.title

    def title(self):
        return self.book_dict['best_book']['title']

    def id(self):
        return int(self.book_dict['best_book']['id']['#text'])

    def publication_year(self):
        return int(self.book_dict['original_publication_year']['#text'])

    def publication_month(self):
        try:
            retval = int(self.book_dict['original_publication_month']['#text'])
        except:
            retval = -1
        return retval

    def author_name(self):
        return self.book_dict['best_book']['author']['name']

    def author_id(self):
        return int(self.book_dict['best_book']['author']['id']['#text'])

    def debug(self):
        print(self.book_dict)

class GR_Auth_Book:
    def __init__(self, book_dict):
        self.book_dict = book_dict

    def __repr__(self):
        return self.title

    def title(self):
        return self.book_dict['title']

    def id(self):
        return int(self.book_dict['id']['#text'])

    def publication_year(self):
        return int(self.book_dict['publication_year'])

    def publication_month(self):
        try:
            retval = int(self.book_dict['publication_month'])
        except:
            retval = -1
        return retval

    def author_name(self):
        if type(self.book_dict['authors']['author']) == list:
            return self.book_dict['authors']['author']['name'] + ' et. al'

        return self.book_dict['authors']['author']['name']

    def author_id(self):
        return int(self.book_dict['authors']['author']['id'])

    def debug(self):
        print(self.book_dict)

    def isbn(self):
        try:
            retVal = self.book_dict['isbn']
        except:
            retval = -1
        return retval

    def isbn13(self):
        try:
            retVal = self.book_dict['isbn13']
        except:
            retval = -1
        return retval
