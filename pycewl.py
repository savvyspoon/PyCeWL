import re
import requests
import re
import time
import click
from bs4 import BeautifulSoup



#speed = 'Medium'
#verbose = True


@click.command()
@click.option('--url', help="URL to run scan against")
@click.option('--speed', type=click.Choice(['Slow', 'Medium', 'Fast']), default="Medium", help="Time between page parsings, Fast=0,Medium=2,Slow=10")
@click.option("--useragent", help="Set custom user-agent. Default = PyCeWL 1.0")
@click.option('--verbose', default=True, help="Set verbosity")
@click.option('--email', 'email', flag_value='email', help="Show emails gathered from spider")

#TODO: Add Commandline Args  -Output,  --emailoutput, 

def cli(url, speed, verbose, useragent, email ):
    
    linklist = []
    wordlist = []
    emaillist = []
    authorlist = []

    if useragent:
        pass
    else:
        useragent = "PyCeWL 1.0"

    linklist.append(url)
    if(verbose == True):
        print(linklist)
    linklist = GetLinks(url, linklist, verbose, useragent)
    for site in linklist:

        if(speed == "Fast"):
            pass
        elif(speed == "Medium"):
            time.sleep(2)
        else:
            time.sleep(10)
        
        wordlist, emaillist, authorlist = ParsePage(site, wordlist, emaillist, authorlist, verbose, useragent)
    #TODO: Create a function to output to file
    print(wordlist)
    if email:
        print(emaillist)

def AddLinkToLinkList(url, linklist, verbose):
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

def AddToWordList(word, wordlist, emaillist, authorlist, verbose):
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

def ParsePage(url, wordlist, emaillist, authorlist, verbose, useragent):
    print(f"Page {url} is being scanned")
    try:
        headers = {'User-Agent': useragent}
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        for text in soup.stripped_strings:
            wordlist, emaillist, authorlist = AddToWordList(text, wordlist, emaillist, authorlist, verbose)
        return wordlist, emaillist, authorlist
    except:
        if(verbose == True):
            print("Error 3")

def GetLinks(url, linklist, verbose, useragent):
    try:
        headers = {'User-Agent': useragent}
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        anchors = soup.find_all('a')

        for a in anchors:
            try:
                newURL = f"{a.attrs['href']}"
                r = re.search("\.", newURL)
                if r:
                    pass
                else:
                    #TODO: Need to parse out the root of the base url so it can append better here if the 
                    #url entered is not a root url.
                    newURL = f"{url}{a.attrs['href']}"
                linklist = AddLinkToLinkList(newURL, linklist, verbose)
            except:
                if(verbose == True):
                    print(f"Couldn't add {newURL} to linklist")
        return linklist
    except:
        if(verbose == True):
            print(f"Error: Something went wrong with {newURL}")
    
if __name__ == "__main__":
    #TODO: Allow for several levels of recursion 
    cli()

    


   

#General TODOs
#TODO: Create a log option
#TODO: Dress up the messaging back to the user. Add color
#TODO: Function to check urls for validity



