lepaul
======
### *A simple python 3 scraper that downloads imgur albums.* ###

lepaul is a program that fetches images from imgur album links and downloads them into a convenient folder wherever you run the script.

### **Usage:**

To run lepaul with default settings simply use the **URL** command:
	
	lepaul.py -u "http://imgur.com/a/tI0m7"

By default, albums will have the name they've been given on Imgur. You can change this with the **name** command:
	
	lepaul.py -u "http://imgur.com/a/tI0m7" -n "Name"
	 
If you only want certain images from an album, you can use **chunkmode** to grab a slice of it:

	lepaul.py -u "http://imgur.com/a/tI0m7" -c
	
lepaul will detect you've activated chunkmode and request integers once it's scraped the data from the Imgur page. This slice includes images at the start and end of the range provided.

You can use all these commands in combination:

	lepaul.py -u "http://imgur.com/a/tI0m7" -c -n "Album"
	
Finally, if you need help you can use the **help** command:

	lepaul.py -h

## Requirements ##

#### *Python 3* ####
<https://www.python.org/downloads/>

#### *Beautiful Soup 4* ####
<https://www.crummy.com/software/BeautifulSoup/>

**Installing BS4 using pip:**

	pip install beautifulsoup4