# imports
import urllib.request
import string
import re

# open the URL using the urllib package
url = "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt"
file = urllib.request.urlopen(url)
# build up a list of the words (remove new space character)
word_list = []
for line in file:
    decoded_line = line.decode("utf-8")
    word_list.append(decoded_line.replace('\n',''))
