# Find New Books

This script works under the assumption that if an author's book has a missing year than it is unpublished or old--both things we are not interested in.

## Setup
1. If you are on ubuntu ensure that you are using `pip3` which can be installed with the command `sudo apt-get install python3-pip`
2. Install the following packages:
  - requests
  - xmltodict
3. Make the main python file executable by running the command `chmod u+x main.py`
4. At the root level of the directory fill in the file secrets.py 

## TDD
- goodreads API
- set up email
-

# Future Notes:
- if getting bad results swap the api call in find books with an api call to author.books. This will require a rework of the books class because the xml looks different
