import re
import requests
import re
import time
from bs4 import BeautifulSoup


linklist = []
wordlist = []
emaillist = []
authorlist = []
speed = 'Medium'
verbose = True

#TODO: Add Commandline Args -url, -speed (SLOW, MEDIUM, FAST), -Output, -Verbose
url = "http://amsurg.com"
linklist.append(url)

def AddLinkToLinkList(url, linklist):
    if(url in linklist):
        if(verbose == True):
            print(f"URL: {url} already in list")
    else:
        urlRoot = url.split("/")
        domainRoot = linklist[0].split("/")
        if(urlRoot[2] == domainRoot[2]):
            linklist.append(url)
            if(verbose == True):
                print(f"URL: {url} added to list")
        else:
            if(verbose == True):
                print(f"URL: {url} is not in scope")
    return linklist

def AddToWordList(word, wordlist, emaillist, authorlist):
    words = word.split(" ")
    for w in words:
        email = re.search(".+\@.+\..+", w)
        if email:
            emaillist.append(w)
        x = re.search("^[a-zA-Z]{4,}$", w)
        if x:
            if(w in wordlist):
                if(verbose == True):
                    print(f"Word: {w} already in list")
            else:
                wordlist.append(w)
        else:
            if(verbose == True):
                print(f"Word: {w} is not a word")
    return wordlist, emaillist, authorlist

def ParsePage(url, wordlist, emaillist, authorlist):
    print(f"Page {url} is being scanned")
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        for text in soup.stripped_strings:
            wordlist, emaillist, authorlist = AddToWordList(text, wordlist, emaillist, authorlist)
        return wordlist, emaillist, authorlist
    except:
        if(verbose == True):
            print("Error 3")

def GetLinks(url, linklist):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        anchors = soup.find_all('a')

        for a in anchors:
            try:
                newURL = f"{a.attrs['href']}"
                r = re.search("\.", newURL)
                if r:
                    pass
                else:
                    newURL = f"{url}{a.attrs['href']}"
                linklist = AddLinkToLinkList(newURL, linklist)
            except:
                if(verbose == True):
                    print(f"Couldn't add {newURL} to linklist")
        return linklist
    except:
        if(verbose == True):
            print(f"Error: Something went wrong with {newURL}")
    
if __name__ == "__main__":
    #TODO: Allow for several levels of recursion 
    if(verbose == True):
        print(linklist)
    linklist = GetLinks(url, linklist)
    for site in linklist:

        if(speed == "Fast"):
            pass
        elif(speed == "Medium"):
            time.sleep(2)
        else:
            time.sleep(10)
        
        wordlist, emaillist, authorlist = ParsePage(site, wordlist, emaillist, authorlist)
    #TODO: Create a function to output to file
    print(wordlist)
    print(emaillist)


   

#General TODOs
#TODO: Create a log option
#TODO: Dress up the messaging back to the user. Add color
#TODO: Function to check urls for validity



