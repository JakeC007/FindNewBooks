#!/usr/bin/python3
"""
April 26, 2020
Author Jake Chanenson
"""

from secrets import key, secret, usrID, jakeEmail
from botmail import send_the_mail
import miscFunc
from datetime import date
import re

def main():
    currentYear = date.today().year
    bookLst = []
    tempBookLst = [] #cheaper to have a temp lst than use list remove--thats O(n)

    #get the list of authors that the user is interested in
    authorLst, authorIDLst = miscFunc.list_user_authors(key, usrID, 'authors-follow')
    print("Pulled List Of Authors")
    print("Grabbing First Author's Books")

    #get list of each author's books, and keep the books that were published within 2 years
    for author in authorIDLst:
        print("Pulling Next Author's Books")
        tempAuthorBooks = miscFunc.list_author_books(key, author)
        for book in tempAuthorBooks:
            if((book.publication_year() >=currentYear-1) and (book.publication_year() <= currentYear)):
                tempBookLst.append(book)

    #grab the user's read shelf. Compare those titles to the titles in the list of author books and keep the unread
    titlesUsrRead = miscFunc.list_user_book_t(key, usrID, 'read')
    for tb in tempBookLst:
        #The two statements logically 'anded' are used for cleaning out junk authors and untitled books
        if((tb.title() not in titlesUsrRead) and (tb.author_name() in authorLst) and (re.search("untitled",tb.title(), re.IGNORECASE) == None )):
            bookLst.append(tb)


    #generate email body
    bodyHTML = f"<html>\n<body\n><p>Hey there!</p>\n <p>Some of your favorite authors have new books out that you haven't read yet:</p>\n <ul>{unpack(bookLst, True)}\n</ul>\n"\
           f"<p>That's {len(bookLst)} new books to read! Remember, these books come from the following authors {authors(authorLst)}. If you wish to change which authors to follow, "\
           f"please edit your shelf entitled <em>authors-follow</em>.</p>\n <p>Happy reading!</p>\n <p>Love,</p>\n <p>The Book Finder Bot</p>\n"\
           f"<p><br></p>\n<p><br></p>\n<p>This email was sent by <em>The Book Finder Bot</em>."\
           f" Its github repo can be found <a href= 'https://github.com/JakeC007/FindNewBooks' rel = 'noopener noreferrer' target='_blank'>here</a></p>\n</body>\n</html>"

    bodyTxt = f"Hey there!\n\n Some of your favorite authors have new books out that you haven't read yet:\n {unpack(bookLst)}\n\n"\
           f"That's {len(bookLst)} new books to read! Remember, these books come from the following authors {authors(authorLst)}. If you wish to change which authors to follow, "\
           f"please edit your shelf entitled 'authors-follow'.\n\n Happy reading!\n\n Love,\n The Book Finder Bot\n"\
           f"\n\nThis email was sent by The Book Finder Bot."\
           f" Its github repo can be found at https://github.com/JakeC007/FindNewBooks"

    send_the_mail(bodyTxt, bodyHTML, jakeEmail)


def unpack(books, HTML = False):
    """
    Pretty string formatting for the books
    @param books - list of book objects
    @return formatted string of books in a list
    """
    retStr = ' '
    for book in books:
        if HTML == True:
            tempStr = '\n\t<li>{0} by {1}</li>'.format(book.title(), book.author_name())
        else:
            tempStr = '\n\t*{0} by {1}'.format(book.title(), book.author_name())
        retStr+=tempStr
    return retStr

def authors(lst):
    """
    Pretty string formatting for the authors
    @param lst - list of author names
    @return formatted string of authors
    """
    retStr = ''
    for i in range(len(lst)):
        if i != len(lst)-1:
            tempStr = '{0}, '.format(lst[i])
        else:
            tempStr = 'and {0}'.format(lst[i])
        retStr+=tempStr
    return retStr

if __name__ == "__main__":
    main()
