# Find New Books

This script works under the assumption that if an author's book has a missing year than it is unpublished or old--both things we are not interested in.

## Setup
1. If you are on ubuntu ensure that you are using `pip3` which can be installed with the command `sudo apt-get install python3-pip`
2. Install the Goodreads package `pip3 install Goodreads`
3. Ensure that all needed dependencies are installed. See the [Goodreads project github page for more information](https://github.com/sefakilic/goodreads)
    -*Warning* The goodraeds project is no longer being maintained.
4.

## TDD
- goodreads API
- set up email
-

# Future Notes:
- if getting bad results swap the api call in find books with an api call to author.books. This will require a rework of the books class because the xml looks different
