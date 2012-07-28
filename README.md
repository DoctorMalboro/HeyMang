Hey Mang!
======

_The easiest way to download all your mangos_


## [Windows Download](http://sourceforge.net/projects/heymang/files/Stable-1.0/Hey%20Mang%21_Win32.exe/download) | [Documentation](https://github.com/DoctorMalboro/HeyMang/wiki) | [Bug tracker](https://github.com/DoctorMalboro/HeyMang/issues) | [Support page](https://sourceforge.net/p/heymang/tickets/)

## Introduction

Hey Mang! is a free, open-source project that allows you to get your manga from your favourite sites.

![HeyMang!](https://github.com/DoctorMalboro/HeyMang/raw/master/screenshots/HeyMang-screenshot02.png)

### 2.0 Future features:
* Threading
* More sites support
* Multiple chapter downloads
* Fully implemented RSS download

### Future sites:
* TBA

## Installation

To install this on windows you only need to use the [windows' installer](http://sourceforge.net/projects/heymang/files/Stable-1.0/Hey%20Mang%21_Win32.exe/download). Linux and other POSIX OS will only need to download the source code and execute it via command line. An example:

	$ tar -xvf DoctorMalboro-HeyMang-a333e24.tar.gz
	$ uniz DoctorMalboro-HeyMang-a333e24.zip # If you download the .zip file
	$ chmod +x programa.py
	$ ./programa.py

And you should have a fully functional **Hey Mang!** working in your POSIX environment.

## Source code deployment:

Want to test and fork this on your own environment? Read the [requirements](https://github.com/DoctorMalboro/HeyMang/wiki/Requirements) first, it'll tell you what you need to install to make this work. Then you just clone the files with a simple:

	git clone git://github.com/DoctorMalboro/HeyMang.git

And you can execute it with the python command line (Read the [function list](https://github.com/DoctorMalboro/HeyMang/wiki/The-Function-List)) like this:

	> python
	> import os
	> from mango import download_mango
	> download_mango(link, os.getcwd()) # You can change this, obviously

Or with the **Hey Mang!** interface, like this:

	> python programa.py

And then choose the folder where you want to save your manga, paste the link, select the option and start downloading!

Remember always to check the official git and to update the program as much as you can.

### Many thanks to:
* All the Python tutorials and the Python documentation that helps to make things easier.
* The libraries I've used: BeautifulSoup and PyQt4.
* The /g/entlemen who help me to change the name.
* StackOverflow for answering all of my questions.
* Everyone who works and contributes to Python.

### License:
**Hey Mang!** is licensed under [BSD Simplified license](http://opensource.org/licenses/bsd-3-clause).