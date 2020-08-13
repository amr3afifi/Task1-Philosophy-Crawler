import urllib
import time
import requests
import string
from bs4 import BeautifulSoup
visitedLinks=[]

# Fn to grab get HTML for every link and It's main body
def htmlParser(wikilink):
    if(wikilink.startswith('/wiki')):
        wikilink="https://en.wikipedia.org"+wikilink

    if (wikilink=="https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy" or wikilink=="https://en.wikipedia.org/wiki/Philosophy" ):
        print("**************** Reached Getting_to_Philosophy ****************")
        exit()

    resp=requests.get(wikilink)
    data=resp.text
    soup = BeautifulSoup(data, "html.parser")
    Content= soup.find(id="mw-content-text").find(class_="mw-parser-output")
    print(wikilink)
    findTags(Content)

# Fn to get the first link and validate it from the main body
def findTags(Content):
    Found=False
    if Content is not None:
        for link in Content.find_all("p", recursive=False):
            if link.find("a", recursive=False):
                LinkEnter=link.find("a", recursive=False).get('href')
                if LinkEnter is not None:
                    if LinkEnter in visitedLinks:
                        print("**************** We are in a Loop ****************")
                        exit()
                    else:
                        Found=True
                        break

    if(Found==True):
        if LinkEnter not in visitedLinks:
            visitedLinks.append(LinkEnter)
        time.sleep(0.5)
        htmlParser(LinkEnter)
    else:
        print("**************** Reached Article without any outgoing Wikilinks ****************")
        exit()

# Starting Position Recursive call Fn
htmlParser("/wiki/Special:Random")
