#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import urllib.request
import urllib
import sys
import os

def imgurWrite(images,albumTitle):
    """Writes the data collected in the imgurParse function."""

    imgNum=1

    print(len(images),"images found.") 
    # try to create a directory based on the album's title
    try:
        os.mkdir(albumTitle)
        print("Folder \""+albumTitle+"\" created.")
        os.chdir(albumTitle)
        for i in images:
            fileName=str("image-{}.png").format(imgNum)    
            imgNum=imgNum+1
            f=open(fileName,'wb')
            f.write(urllib.request.urlopen(i).read())
            f.close()
            print("#",i,"has been successfully downloaded.")
    except FileExistsError:
        print("[*] You already have an album or folder by this name!")

def imgurChunk(images,albumTitle,chunkStart,chunkEnd):
    """Grabs a chunk of the album, as specified in the main function."""

    imgNum=1

    print(len(images),"images found.")
    print("Cutting out the chunk...")
    chunk = images[chunkStart:chunkEnd]
    print("Chunk contains",len(chunk),"images.")
    imgurWrite(chunk,albumTitle)

def imgurParse(albumURL,chunkMode):
    """Parses the html for use in the imgurWrite function."""

    # there's probably a better name for this list
    images=[]
    
    try:
        req=urllib.request.Request(albumURL)
        res=urllib.request.urlopen(req)
        # here we scrape and extract
        # whatever we need
        req
        albumData=BeautifulSoup(res,'html.parser')
        if "-n" in sys.argv:
            nLocate=sys.argv.index('-n')
            albumTitle=str(sys.argv[nLocate+1])
        else:
            albumTitle=albumData.title.string[:-17].lstrip()
        # this for loop gathers the images and compiles them into
        # a list called images if they're what we're looking for
        for img in albumData.find_all('img'):
            getURL=img.get('src')
            imgURL="//i.imgur.com/"
            if imgURL in getURL:
                newURL=str("http:"+getURL)
                images.append(newURL)
        if chunkMode == True:
            print("Chunk mode is active.")
            chunkStart=int(input("<#lepaul>Chunk Start: "))
            chunkEnd=int(input("<#lepaul>Chunk End: "))
            print("[*] lepaul requires an integer for chunk mode.")
            imgurChunk(images,albumTitle,chunkStart-1,chunkEnd)
        else:
                imgurWrite(images,albumTitle)
    except (urllib.error.URLError,urllib.error.HTTPError):
        print("[*] Invalid URL: lepaul needs an imgur album URL to work!") 
    except ValueError:
        print("[*] Invalid Input: chunkmode needs to be provided with integers!")

def main():
    """Handles user input and prints help/usage info."""
    
    chunkMode = False
    usage="lepaul.py -u \"http://www.imgur.com/a/babpls\" -h --help -c --chunkmode -n --name"
    usageHelp="""
    lepaul is a python script for grabbing images from an imgur album.
    Simply provide it with an imgur album url and it'll do the rest for you!
    by the jukebox

    Commands
    ========
    -u      allows you to input a url.
    -c      activates chunkmode.
    -n      allows you to set the name of an album folder.
    -h      displays this help text.

    usage examples:
        lepaul.py -u "http://www.imgur.com/a/album"
        lepaul.py -u "http://www.imgur.com/a/album" -c
        lepaul.py -u "http://www.imgur.com/a/album" -n "New Album"
        lepaul.py -u "http://www.imgur.com/a/album" -c -n "New Album"
    """
    
    # check over the args and make sure everything is in order.
    if len(sys.argv) >= 2: 
        if "-h" in sys.argv:
            print(usageHelp)
        elif sys.argv[1] == "-u":
            # check the user input make sure we're
            # getting an imgur album
            try:
                if "-c" in sys.argv:
                    chunkMode = True
                else:
                    chunkMode = False
                if str("imgur.com/a/") in sys.argv[2]:
                    imgurParse(sys.argv[2],chunkMode)
                else:
                    print("[*] Invalid URL: lepaul needs an imgur album URL to work!")
            except IndexError:
                print("[*] Invalid Input: lepaul requires more arguments!"
                        "\n"+usage)
    else:
        print(usage)

main()

