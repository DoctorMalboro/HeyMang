Hey Mang!
======

## The easiest way to download all your mangos ##

Hey Mang! is a free, open-source project that allows you to get your manga from your favourite sites.

![HeyMang!](https://github.com/DoctorMalboro/HeyMang/raw/master/HeyMang-preview.png "Hey Mang!")

### Future features:
* RSS downloads **(Implemented in version 0.9 Beta)**
* Update checker **(Implemented in version 0.9 Beta)**
* [See full list](https://github.com/DoctorMalboro/HeyMang/issues/6)

### Future sites:
* Mangafox **(Implemented on version 0.7 Beta)**
* Batoto **(Implemented on version 0.8 Beta)**
* ExHentai
* E-Hentai **(Implemented on version 0.9 Beta)**
* [See full list](https://github.com/DoctorMalboro/HeyMang/issues/1)

### Deployment:

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