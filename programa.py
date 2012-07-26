import PyQt4
import sys
import mango
import images_rc
from feed import rss_feed
from PyQt4 import QtGui
from PyQt4 import QtCore
from mango import download_mango2, check_version

CURRENT_VERSION = '0.9 Beta'

class HelloWindow(QtGui.QMainWindow):

    def __init__(self, win_parent = None):
        QtGui.QMainWindow.__init__(self, win_parent)
        self.create_widgets()

    def create_widgets(self):

        # Menubar function
        # Change path option
        changePath = QtGui.QAction(QtGui.QIcon(':/img/folder-icon.png'), '&Change folder', self)
        changePath.setShortcut('Ctrl+P')
        changePath.triggered.connect(self.browseDir)
        # RSS download option
        RSSDownload = QtGui.QAction(QtGui.QIcon(':/img/RSS-icon.png'), '&RSS Downloader', self)
        RSSDownload.setShortcut('Ctrl+R')
        RSSDownload.triggered.connect(self.RssDownloader)
        # Exit option
        exitOption = QtGui.QAction(QtGui.QIcon(':/img/exit-icon.png'), '&Exit', self)
        exitOption.setShortcut('Ctrl+Q')
        exitOption.triggered.connect(QtGui.qApp.quit)
        # About option
        aboutOption = QtGui.QAction(QtGui.QIcon(':/img/about-icon.png'), '&About Hey Mang!', self)
        aboutOption.triggered.connect(self.aboutManget)
        # License option
        licenseOption = QtGui.QAction(QtGui.QIcon(':/img/license-icon.png'), '&Hey Mang! License', self)
        licenseOption.triggered.connect(self.MangetLicense)

        # Setting the menubar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        helpMenu = menubar.addMenu('&Help')
        fileMenu.addAction(changePath)
        fileMenu.addAction(RSSDownload)
        fileMenu.addAction(exitOption)
        helpMenu.addAction(aboutOption)
        helpMenu.addAction(licenseOption)

        self.label = QtGui.QLabel('Manga link:')
        self.linkEdit = QtGui.QLineEdit()
        self.linkButton = QtGui.QPushButton('Download')
        self.pathLabel = QtGui.QLabel('Saving path:')
        self.pathLabel.move(100, 100)
        self.pathEdit = QtGui.QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.pathLabel2 = QtGui.QLabel(self.pathEdit)
        self.path2 = str(self.pathEdit)
        self.service = QtGui.QComboBox()
        self.service.addItem('MangaReader')
        self.service.addItem('MangaFox')
        self.service.addItem('Batoto')
        self.service.addItem('E-Hentai')

        if not self.pathEdit:
            sys.exit(1)

        QtCore.QObject.connect(self.linkButton, QtCore.SIGNAL('clicked()'), self.on_link_clicked)

        grid = QtGui.QGridLayout()
        grid.addWidget(self.label, 1, 0)
        grid.addWidget(self.linkEdit, 1, 1)
        grid.addWidget(self.linkButton, 1, 2)
        grid.addWidget(self.service, 1, 3)
        grid.addWidget(self.pathLabel, 2, 0)
        grid.addWidget(self.pathLabel2, 2, 1)

        centralWidget = QtGui.QWidget()
        centralWidget.setLayout(grid)
        self.setCentralWidget(centralWidget)

        self.setGeometry(300, 300, 600, 100) # position-x, position-y, width, height
        self.setWindowTitle('Hey Mang! v%s' % CURRENT_VERSION) # Title
        self.setWindowIcon(QtGui.QIcon(':/img/manga-icon.png')) # Icon

    def browseDir(self):
        directory = QtGui.QFileDialog.getExistingDirectory(self, 'Select a new directory')
        self.pathEdit.replace(self.pathEdit, directory)
        self.pathLabel2.setText(directory)

    def RssDownloader(self):
        link = QtGui.QInputDialog.getText(self, 'Input Dialog', 'RSS feed link:')

        if link[0]:
            c = str(link[0])
            a = QtGui.QMessageBox(self)
            a.setWindowTitle('The link')
            rss_feed(c, self.path2)
            a.setText('Downloading your shit')
            a.setGeometry(450, 300, 200, 150)
            a.show()

    def aboutManget(self):
        about = QtGui.QMessageBox(self)
        about.about(self, 'About Hey Mang!', """Hey Mang! is a free, open-source project that allows you to get your manga from your favourite sites. Right now is at beta stage and so many features are not yet implemented and many sites have not been covered yet.

Future features:
    *RSS downloads
    *Better image tagging
    *Auto-update (only for stable branches)

Future sites:
    *ExHentai

Remember always to check the official git and to update the program as much as you can. Fork, pull requests and issue bugs, that always helps.

Many thanks to:
    *All the Python tutorials and the Python documentation that helps to make things easier.
    *The libraries I've used: BeautifulSoup and PyQt4.
    *The /g/entlemen who help me to change the name.
    *StackOverflow for answering all of my questions.
    *Everyone who works and contributes to Python, a beautiful and excellent language!""")

    def MangetLicense(self):
        license = QtGui.QMessageBox(self)
        license.setWindowTitle('Hey Mang! License')
        license.setText("""
Copyright (c) 2012, Leandro Poblet
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
            * Redistributions of source code must retain the above copyright
              notice, this list of conditions and the following disclaimer.
            * Redistributions in binary form must reproduce the above copyright
              notice, this list of conditions and the following disclaimer in the
              documentation and/or other materials provided with the distribution.
            * Neither the name of the Leandro Poblet nor the
              names of its contributors may be used to endorse or promote products
              derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Leandro Poblet BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.""")
        license.sizeHint()
        license.show()

    def checkVersion(self):
        version = QtGui.QMessageBox(self)
        version.setWindowTitle('Hey Mang! Version')
        check_version('', CURRENT_VERSION)
        if check_version == 'Outdated':
            version.setText('Hey Mang! is up-to-date.')
            version.show()
        else:
            version.setText('Your Hey Mang! version is outdated. Please update it inmediately.')

    def on_link_clicked(self):
        self.a = self.linkEdit.displayText()
        self.service = self.service.currentText()
        download_mango2(self.a, self.path2, self.service)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = HelloWindow()
    mainWindow.show()
    app.exec_()