import requests
import time
from bs4 import BeautifulSoup
import webbrowser
import os
#Ideas
# From here make a small menu program that reads you the names of tricks, and links you to them appropriatly
# Have it ask what tricks youve learned and store them in a file
# In the future: Store learned tricks in SQL Database#
web = requests.get("http://libraryofjuggling.com/Home.html")
soup = BeautifulSoup(web.text,'html.parser')
#webbrowser.open_new("http://libraryofjuggling.com/Home.html")
for tricks in soup.find_all('a'):
    print(tricks)
