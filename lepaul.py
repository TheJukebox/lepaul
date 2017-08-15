#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import urllib.request
import urllib
import sys
import os

urlError="[*] Invalid URL! You need to point lepaul to a valid imgur album URL."

def imgurWrite(images):
    """Writes the data collected in the imgurParse function."""

    imgNum=1
    for i in images:
        fileName=str("image-{}.png").format(imgNum)    
        imgNum=imgNum+1
        f=open(fileName,'wb')
        f.write(urllib.request.urlopen(i).read())
        f.close()
        print("#",i,"has been successfully downloaded.")

def imgurParse(albumURL):
    """Parses the html for use in the imgurWrite function."""

    global urlError
    # there's probably a better name for this list
    images=[]
    
    try:
        req=urllib.request.Request(albumURL)
        res=urllib.request.urlopen(req)
        # here we scrape and extract
        # whatever we need
        try:
            req
            albumData=BeautifulSoup(res,'html.parser')
            albumTitle=albumData.title.string[:-17].lstrip()
            # try to create a directory based on the album's title
            try:
                os.mkdir(albumTitle)
                print("Folder \""+albumTitle+"\" created.")
                os.chdir(albumTitle)
            except FileExistsError:
                print("[*] You already have an album or folder by this name!")
            # this for loop gathers the images and compiles them into
            # a list called images if they're what we're looking for
            for img in albumData.find_all('img'):
                getURL=img.get('src')
                imgURL="//i.imgur.com/"
                if imgURL in getURL:
                    newURL=str("http:"+getURL)
                    images.append(newURL)
            imgurWrite(images)
        except urllib.error.HTTPError:
            print(urlError) 
    except (urllib.error.URLError,ValueError):
        print(urlError) 

def main():
    """Handles user input and prints help/usage info."""
    
    global urlError
    usage="lepaul.py -u \"http://www.imgur.com/a/babpls\" -h --help"
    usageHelp="""
    lepaul is a python script for grabbing images from an imgur album.
    Simply provide it with an imgur album url and it'll do the rest for you!
    by the jukebox

    Commands
    ========
    -u      allows you to input a url.
    -h      displays this help text.

    usage examples:
        lepaul.py -u "http://www.imgur.com/a/album"
    """
    
    # check over the args and make sure everything is in order.
    if len(sys.argv) >= 2: 
        if "-h" in sys.argv:
            print(usageHelp)
        elif sys.argv[1] == "-u":
            # check the user input make sure we're
            # getting an imgur album
            try:
                if str("imgur.com/a/") in sys.argv[2]:
                    imgurParse(sys.argv[2])
                else:
                    print(urlError)
            except IndexError:
                print("Invalid number of arguments."
                        "\n"+usage)
    else:
        print(usage)

main()

