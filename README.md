# Find New Books Bot

![Goodreads Logo](http://s.gr-assets.com/assets/icons/goodreads_icon_50x50-823139ec9dc84278d3863007486ae0ac.png)  <img src="https://cdn3.iconfinder.com/data/icons/avatars-9/145/Avatar_Robot-512.png" alt="icon of robot" width="50" height="50">


## What is it?
This bot finds new books from authors that you follow, checks to see if you have read those books, and sends you an email with a list of the new books that you haven't read.

## How it works
This bot uses information from a Goodread users public *read* shelf to find out what books a user has read. To find out what authors a user is interested, the bot looks for another shelf created by the user called *authors-follow*. It uses these two sets of information plus your email address to send you the list of recently published unreadbooks.

## Disclaimers
- This script works under the assumption that if an author's book has a missing year than it is unpublished or old--both things we are not interested in.
- ***If Goodreads passes the program garbage data then the program will email you garbage data.***
    - Sometimes there are reissuing of books or Goodreads just has the incorrect year. This causes the email to contain some books that you may not expect to be there. If Goodreads says that a book was published within the last year or so then, assuming the book is unread, that book goes in the email.   
- This program is not affiliated in anyway with Goodreads.

# Getting this script to work for you

## Goodreads Setup
1. The script pulls in the list of authors that you are interested in by looking at a shelf entitled *authors-follow*. As such one of the shelves associated with the user (identified with the Goodreads `userID`) must have a shelf called *authors-follow*. Please create a shelf called *authors-follow* and fill it with one book from each of the authors that you want the script to look for.  
2. The script checks against a user's *read* shelf to see what books by the authors listed in the authors-follow* shelf the user has read. Thus, please ensure that the **user's *read* shelf is up to date**

## Technical Setup
0. Get a copy of the repository locally repository
1. If you are on ubuntu ensure that you are using `pip3` which can be installed with the command `sudo apt-get install python3-pip`
2. Install the following packages via `pip`:
    - requests
    - xmltodict
3. Make `main.py` executable by running the command `chmod u+x main.py`
4. At the root level of the directory rename secrets2.py to secrets.py then open the file and fill in the fields.
5. Run `main.py` with the command `./main.py`

## Possible Future Extensions
- add function for other users to enter their user ID
- fork for web app?
