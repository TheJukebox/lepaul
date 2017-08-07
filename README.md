lepaul
======
## *A simple scraper that downloads imgur albums.*

lepaul is a program that fetches images from imgur album links and downloads them into a convenient folder wherever you run the script.

Usage:
    
    lepaul.py -u "http://imgur.com/a/tI0m7"
   lepaul will run, fetch the images, and create a folder wherever lepaul.py is located.
   The folder will have the same name as the album on imgur. Each image in the album will be numbered
   according to its location in the album, so beware of albums that are backwards or otherwise out of order if
   you like to keep your images organised.
   
    lepaul.py -h
   This will display all the help you need (if you really need it) to run lepaul.
