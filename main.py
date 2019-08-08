import requests
import time
from bs4 import BeautifulSoup
import webbrowser
from funcs import menus as mn

links = {}
tricks = list()
htmllinks = list()
number_of_tricks = 177
menu_choice = 0

def loadTricks(soup,web):
    unwanted_menu = 0
    counter = 0
    #Loop through anchor tags in website, limited to 177 to stop from including extraneous links
    #Starts at 3 for this reason also
    for names in soup.find_all('a',limit = number_of_tricks):
        unwanted_menu += 1
        if(unwanted_menu > 3):
        #Can use these lists later
         tricks.append(names.string)
         htmllinks.append(names.get('href'))
         links.update({tricks[counter] : htmllinks[counter]})
         counter += 1
        else:
            continue
#Ideas
# From here make a small menu program that reads you the names of tricks, and links you to them appropriatly
# Have it ask what tricks youve learned and store them in a file
# In the future: Store learned tricks in SQL Database#
web = requests.get("http://libraryofjuggling.com/Home.html")
soup = BeautifulSoup(web.text,'html.parser')
data = open("data.txt","r")
loadTricks(soup,web)
#webbrowser.open_new("http://libraryofjuggling.com/Home.html")  
while menu_choice != '3':
    numb_list = 0 
    mn.main_menu()
    menu_choice = input("\nType your selection: ")
    if menu_choice == '1':
        mn.display_tricks(tricks)
