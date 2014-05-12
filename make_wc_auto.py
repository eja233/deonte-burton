#!/usr/bin/env python2
from bs4 import BeautifulSoup
import urllib2
from os import path
import sys
import wordcloud
from readability.readability import Document	

d = path.dirname(__file__)

# String to hold the text from the webpages. 
text = "";

# Array of webpages which we'll loop through (from googling Deonte Burton draft).
url_list = ["http://www.draftexpress.com/profile/Deonte-Burton-6487/", 
            "http://blogs.rgj.com/chrismurray/2014/01/10/nba-scouts-view-nevadas-deonte-burton-as-solid-draft-pick-but-not-a-first-rounder/", 
            "http://www.nbadraftroom.com/2014/01/deonte-burton.html", 
            "http://www.nbadraftinsider.com/deonte-burton/", 
            "http://nbaprospects.blogspot.com/2012/08/scouting-report-deonte-burton-nevada.html",
            "http://rushthecourt.net/2014/01/09/a-college-basketball-resolution-for-2014-get-to-know-nevadas-deonte-burton/",
            "http://mrsportsblog.wordpress.com/2014/03/05/trust-me-on-this-dynamic-deonte-burton-of-nevada-will-be-making-a-living-in-the-nba/", 
            "http://www.draftexpress.com/article/NBA-Draft-Prospect-of-the-Week-Deonte-Burton-4392/",
            "http://www.nevadawolfpack.com/sports/m-baskbl/spec-rel/021214aad.html"] 

# Loop through url items and get the text from each. 
for url in url_list:
    content = urllib2.urlopen(url)

    text += Document(content).summary() + " "

# Separate into a list of word, frequency).
words = wordcloud.process_text(text)

# Compute the position of the words. 
elements = wordcloud.fit_words(words)

# Draw the positioned words to a PNG file. 
wordcloud.draw(elements, path.join(d, 'db2.png'))