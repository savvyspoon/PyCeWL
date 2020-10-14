import requests
import time
import re
from bs4 import BeautifulSoup


linklist = []
wordlist = []
emaillist = []
authorlist = []

depth = 2

#TODO: Use the click package to take in arguments
url = "https://www.duanewaddle.com/"

linklist.append(url)

def AddLinkToLinkList(url, linklist):
    if(url in linklist):
        print(f"URL: {url} already in list")
    else:
        urlRoot = url.split("/")
        domainRoot = linklist[0].split("/")
        if(urlRoot[2] == domainRoot[2]):
            linklist.append(url)
            print(f"URL: {url} added to list")
        else:
            print(f"URL: {url} is not in scope")
    return linklist

def AddToWordList(word, wordlist):
    print(word)
    words = word.split(" ")
    for w in words:
        x = re.search("[a-zA_Z]{4,}", w)
        #TODO: Remove Special Characters
        if x:
            if(w in wordlist):
                print(f"Word: {w} already in list")
            else:
                wordlist.append(w)
        else:
            print(f"Word: {w} is not a word")
    return wordlist

def AddEmailtoEmailList(email, emaillist):
    pass

def AddAuthortoAuthorList(author, authorlist):
    pass

def ParsePage(url, wordlist, emaillist, authorlist):
    print(f"Page {url} is being scanned")
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        for text in soup.stripped_strings:
            #TODO: Check if its an email
            #TODO: Check if its a document
            wordlist = AddToWordList(text, wordlist)
        return wordlist
    except:
        #TODO: Better Error messages
        print("Error 3")

def GetLinks(url, linklist):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        anchors = soup.find_all('a')

        for a in anchors:
            try:
                newURL = f"{a.attrs['href']}"
                linklist = AddLinkToLinkList(newURL, linklist)
            except:
                print("Error 1")
        return linklist
    except:
        print("Error 2")
    


if __name__ == "__main__":
    #TODO: Allow for several levels of recursion 
    linklist = GetLinks(url, linklist)
    
    for site in linklist:
        ParsePage(site, wordlist, emaillist, authorlist)
    print(wordlist)
    


   

#General TODOs
#TODO: Create a log option
#TODO: Dress up the messaging back to the user
#TODO: Async



# Get a website from commandline or file

#Create method to handle words being put to it

#Scan the website for documents and links

#For each link

    #Handle Documents
        #check for metadata about author
        #check for email addresses
        #Get list of words

    #Handle sites
        #check for email addresses
        #Get list of words

