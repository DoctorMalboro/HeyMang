import os # Global OS variables
import sys # System arguments and variables
import urllib2 # Opening of links
import re # Regex reader
from bs4 import BeautifulSoup # HTML parser
from os.path import basename # Filename base name
from urlparse import urlsplit # Link splitter (ninja-style)

# Path Changer Function
def pathchange(old, new):
    if not(os.path.exists(new)):
        os.mkdir(new)
    os.chdir(new)

# Download function
def download_mango(url, path):   

    pathchange(os.getcwd(), path) # We change the path of the image to be saved
    urlContent = urllib2.urlopen(url).read() # We read the URL
    s = int(url[-1:]) # Read the last number (page id)
    imgUrls = re.findall('img .*?src="(.*?)"', urlContent) # We read the mango
    

    # And we open the loop...
    for imgUrl in imgUrls:
        try:
            imgData = urllib2.urlopen(imgUrl).read() # We open the image and read it
            fileName = basename(urlsplit(imgUrl)[2]) # We split the name and create the file
            output = open(fileName, 'wb') # We open it
            output.write(imgData) # We save it
            output.close() # We close it!
        except IOError: # No file? No disk? Okay, check that out
            print "File not found or full disk. Try again."
            sys.exit(1)
        except KeyboardInterrupt:
            print "Operation aborted manually."
            sys.exit(1)
        except:
            print "Unknown error. If this persists, contact the author or create a ticket in the bugtracker."
            sys.exit(1)

# Main function
def main():
    url = sys.argv[1] # Pardon my ignorance, but I use this because I have not come with a better solution yet
    name = url.strip('/').split('/') # We split all the / from the name
    name = name[len(name)-2] # And we clean up the name
    chapter = int(url[-1:])
    path = os.getcwd() + '\\' + '%s - chapter %d' % (name, chapter) # Path to save your animu

    page = urllib2.urlopen(url).read() # We read the page
    soup = BeautifulSoup(page) # And we add it to the soup!

    url = url + '/' # Little something to start downloading the pages!
    
    soup = soup.findAll('option') # We select all the option tags
    for l in soup: # And we start with a loop
        l = l.get_text()
        url2 = url + str(l)
        download_mango(url2, path)

if __name__ == '__main__':
    main()
