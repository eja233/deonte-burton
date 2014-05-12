#!/usr/bin/env python2
from bs4 import BeautifulSoup
import urllib2
from os import path
import sys
import wordcloud

d = path.dirname(__file__)

# String to hold the text from the webpages. 
text = open(path.join(d, 'deonte.txt')).read()

# Separate into a list of word, frequency).
words = wordcloud.process_text(text)

# Compute the position of the words. 
elements = wordcloud.fit_words(words)

# Draw the positioned words to a PNG file. 
wordcloud.draw(elements, path.join(d, 'deonte2.png'))