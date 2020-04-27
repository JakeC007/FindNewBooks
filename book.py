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
