"""
====================================
====================================
============ Hey Mang! =============
====================================
====================================
===== Created by DoctorMalboro =====
====================================
====================================
============= License: =============
====================================
====================================
====== BSD Simplified License ======
====================================
====================================
=========== Repository: ============
====================================
====================================
=== github/DoctorMalboro/HeyMang ===
====================================
====================================
"""

import os 
import sys
import urllib2
import re
import threading
from bs4 import BeautifulSoup
from os.path import basename
from urlparse import urlsplit

def pathchange(old, new):
    """
        Function: patchange(old, new)
        Usage: pathchange(os.getcwd(), '/My/Working/Directory')
        Added in version: 0.3 Beta
    """
    if sys.platform.startswith('win'):
        if not(os.path.exists(new)):
            os.mkdir(new)
        os.chdir(new)
    elif sys.platform.startswith('linux'):
        if not(os.path.exists(new)):
            os.mkdir(new)
        os.fchdir(new)

def check_version(link, version):
    a = urllib2.urlopen(link).read()
    b = str(version)
    if a == b:
        return 'Updated'
    else:
        return 'Outdated'

def download_mango(url, path):   
    """
        Function: download_mango(url, path)
        Usage: download_mango('http://www.mangareader.net/poyopoyo-kansatsu-nikki', os.getcwd())
        Added in version: 0.1 Beta
    """
    if path != os.getcwd():
        pathchange(os.getcwd(), path)
    urlContent = urllib2.urlopen(url).read()
    imgUrls = re.findall('img .*?src="(.*?.jpg)"', urlContent)


    for imgUrl in imgUrls:
        try:
            imgData = urllib2.urlopen(imgUrl).read()
            fileName = basename(urlsplit(imgUrl)[2])
            output = open(fileName, 'wb')
            output.write(imgData)
            output.close()
        except IOError: 
            print "File not found or full disk. Try again."
            sys.exit(1)
        except KeyboardInterrupt:
            print "Operation aborted manually."
            sys.exit(1)
        except:
            print "Unknown error. If this persists, contact the author or create a ticket in the bugtracker."
            sys.exit(1)

def recognise_mangareader(link, path):
    """
        Function: recognise_mangareader(link, path)
        Usage: recognise_mangareader('http://www.mangareader.net/poyopoyo-kansatsu-nikki', os.getcwd())
        Added in version: 0.4 Beta
    """
    page = urllib2.urlopen(link).read()
    soup = BeautifulSoup(page)

    soup = soup.findAll(id='listing')
    for s in soup:
        s = s.findAll('td')
        for t in s:
            t = t.findAll('a')
            for x in t:
                 link = 'http://www.mangareader.net' + x.get('href')
                 link = re.split('\n', link)
                 for dummy in link:
                    w = urllib2.urlopen(dummy).read()
                    soup = BeautifulSoup(w)
                    soup = soup.findAll('option')
                    for alpha in soup:
                        alpha = alpha.get_text()
                        print alpha
                        url = dummy + '/' + str(alpha)
                        download_mango(url, path)
                 
def recognise_mangafox(link, path):
    """
        Function: recognise_mangafox(link, path)
        Usage: recognise_mangafox('http://mangafox.me/manga/tari_tari/', os.getcwd())
        Added in version: 0.7 Beta
    """
    url = str(link)
    url2 = re.findall('/([0-9]+).html', url)
    page = urllib2.urlopen(url).read()

    soup = BeautifulSoup(page)

    catalog = soup.findAll('ul')
    for content in catalog:
        content = content.findAll('h3')
        for links in content:
            links = links.findAll('a')
            for extract in links:
                extract = extract.get('href')

                page = urllib2.urlopen(extract).read()

                soup = BeautifulSoup(page)

                soup = soup.findAll('option')
                a = max(soup)
                a = soup.index(a)
                c = 0
                while (c < a):
                    c = c + 1
                    d = re.sub('\d+.html', '', extract)
                    d = d + str(c) + '.html'
                    download_mango(d, path)

def recognise_batoto(link, path):
    """
        Function: recognise_batoto(link, path)
        Usage: recognise_batoto('http://www.batoto.net/comic/_/comics/china-girl-r1935', os.getcwd())
        Added in version: 0.8 Beta
    """
    url = str(link)
    page = urllib2.urlopen(url).read()

    soup = BeautifulSoup(page)

    catalog = soup.findAll('table', 'chapters_list')
    for blocks in catalog:
        blocks = blocks.findAll('td')
        for links in blocks:
            links = links.find_all('a')
            for mangas in links:
                if mangas.string == None:
                    mangas = mangas.get('href')

                    page = urllib2.urlopen(mangas).read()

                    soup = BeautifulSoup(page)

                    soup = soup.find_all(id='page_select')
                    soup = soup[0].get_text()
                    b = re.findall(r'\d+', soup)
                    for c in b:
                        d = mangas + '/' + c
                        download_mango(d, path)


def download_eHentai(link, path):

    if path != os.getcwd():
        pathchange(os.getcwd(), path)

    url = str(link)
    url = urllib2.urlopen(url).read()

    soup = BeautifulSoup(url)

    soup = soup.find_all('img')
    soup = soup[4].get('src')
    filename = basename(urlsplit(link)[2] + '.jpg')
    image = urllib2.urlopen(soup).read()
    output = open(filename, 'wb')
    output.write(image)
    output.close()


def recognise_eHentai(link, path):
    url = str(link)
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page)
    name = soup.findAll('title')
    name = name[0].get_text().encode('utf-8')
    name = str(name)
    path = path + '\\' + name
    download_eHentai(link, path)

    pages = soup.find_all('span')
    pages = pages[1].get_text()
    pages = int(pages)
    z = 0

    while (pages > z):
        z = z + 1
        sopa = soup.find('div', 'sn')
        sopa = sopa.find_all('a')
        sopa = sopa[2].get('href')

        url = str(sopa)
        download_eHentai(url, path)
        page = urllib2.urlopen(url).read()

        soup = BeautifulSoup(page)

        sopa = soup.find('div', 'sn')
        sopa = sopa.find_all('a')
        sopa = sopa[2].get('href')
        download_eHentai(sopa, path)


def download_mango2(url, path, service):
    """
        Function: download_mango2(url, path, service)
        Usage: download_mango2('http://www.batoto.net/read/_/83396/k-on_v1_by_houkago-translations', os.getcwd(), 'Batoto')
        Added in version: 0.6 Beta
    """
    url = str(url)
    if service == 0:
        name = url.strip('/').split('/')
        name = name[3]
        name = name.replace('-', ' ')
        name = name.capitalize()
        chapter = int(url[-1:])
        path = str(path) + '\\' + '%s - chapter %d' % (name, chapter)
        recognise_mangareader(url, path)
    elif service == 1:
        name = url.strip('/').split('/')
        name = str(name[4])
        name = name.replace('_', ' ')
        name = name.capitalize()
        a = re.findall('/c([0-9]+)/', url)
        chapter = a[0]
        chapter = int(chapter)
        path = str(path) + '\\' + '%s - chapter %d' % (name, chapter)
        recognise_mangafox(url, path)
    elif service == 2:
        name = url.strip('/').split('/')
        name = name[-1:]
        for s in name:
            s = s.replace('_', ' ')
            s = s.capitalize()
            path = str(path) + '\\' + '%s' % s
            recognise_batoto(url, path)
    elif service == 3:
        recognise_eHentai(url, path)
    else:
        print 'Service not available. Try again'
        sys.exit()