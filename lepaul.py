#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import urllib.request
import urllib
import sys
import os

urlError="[*] Invalid URL! You need to point lepaul to a valid imgur album URL."

def albumDL(albumURL):
    """Downloads the album."""
    
    global urlError
    imgNum=0

    try:
        req=urllib.request.Request(albumURL)
        res=urllib.request.urlopen(req)
        try:
            req
            albumData=BeautifulSoup(res,'html.parser')
            albumTitle=albumData.title.string
            try:
                os.mkdir(albumTitle.lstrip())
                os.chdir(albumTitle.lstrip())
                print("Folder \""+albumTitle.lstrip()+"\" created.")
                for image in albumData.find_all('img'):
                    getURL=image.get('src')
                    imgURL="//i.imgur.com/"
                    imgNum=imgNum+1
                    if imgURL in getURL:
                        newURL=str("http:"+getURL)
                        fileName=str('image-{}.png').format(imgNum)
                        f=open(fileName,'wb')
                        f.write(urllib.request.urlopen(newURL).read())
                        f.close()
                        print(newURL,"has been successfully downloaded.")
            except FileExistsError:
                print("You already have an album by this name!") 
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

    if len(sys.argv) >= 2: 
        if "-h" in sys.argv:
            print(usageHelp)
        elif sys.argv[1] == "-u":
            try:
                if str("imgur.com/a/") in sys.argv[2]:
                    albumDL(sys.argv[2])
                else:
                    print(urlError)
            except IndexError:
                print("Invalid number of arguments."
                        "\n"+usage)
    else:
        print(usage)

main()

