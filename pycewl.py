import requests
import time
from bs4 import BeautifulSoup


linklist = []
wordlist = []
emaillist = []
authorlist = []

depth = 2

url = "https://www.duanewaddle.com/"

linklist.append(url)

def AddLinkToLinkList(url, linklist):
    if(url in linklist):
        print(f"URL: {url} already in list")
    else:
        linklist.append(url)
        print(f"URL: {url} added to list")
    return linklist

def AddToWordList(word, wordlist):
    pass

def AddEmailtoEmailList(email, emaillist):
    pass

def AddAuthortoAuthorList(author, authorlist):
    pass

def ParsePage(url, wordlist, emaillist, authorlist):
    print(f"Page {url} is being scanned")

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
    print(linklist)
    counter = 0
    while counter < depth:
        counter = counter + 1
        print(f"Counter at {counter}")
        time.sleep(3)
        for url in linklist:
            linklist = GetLinks(url, linklist)


   





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

