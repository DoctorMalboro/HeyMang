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

    if path != os.getcwd():
        pathchange(os.getcwd(), path) # We change the path of the image to be saved
    urlContent = urllib2.urlopen(url).read() # We read the URL
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

def recognise_mangareader(link, path):
    page = urllib2.urlopen(link).read() # We read the page
    soup = BeautifulSoup(page) # And we add it to the soup!

    link = link + '/' # Little something to start downloading the pages!
    
    soup = soup.findAll('option') # We select all the option tags
    for l in soup: # And we start with a loop
        l = l.get_text()
        url2 = link + str(l)
        download_mango(url2, path)

def recognise_mangafox(link, path):
    url = str(link)
    url2 = re.findall('/([0-9]+).html', url)
    page = urllib2.urlopen(url).read()

    soup = BeautifulSoup(page)

    soup = soup.findAll('option')
    a = max(soup)
    b = soup.index(a)
    c = 0
    while (c < b):
        c = c + 1
        d = re.sub('\d+.html', str(c), url)
        d = d + '.html'
        download_mango(d, path)
    

# Main function
def download_mango2(url, path, service):
    url = str(url)
    if service == 'mangareader':
        name = url.strip('/').split('/')
        name = name[3]
        name = name.replace('-', ' ')
        name = name.capitalize()
        chapter = int(url[-1:])
        path = str(path) + '\\' + '%s - chapter %d' % (name, chapter)
        recognise_mangareader(url, path)
    elif service == "mangafox":
        name = url.strip('/').split('/')
        name = str(name[4])
        name = name.replace('_', ' ')
        name = name.capitalize()
        a = re.findall('/c([0-9]+)/', url)
        chapter = a[0]
        chapter = int(chapter)
        path = str(path) + '\\' + '%s - chapter %d' % (name, chapter)
        recognise_mangafox(url, path)
    else:
        print 'Service not available. Try again'
        sys.exit()