import PyQt4
import sys
import mango
from PyQt4 import QtGui
from PyQt4 import QtCore
from mango import download_mango2


class HelloWindow(QtGui.QMainWindow):

    def __init__(self, win_parent = None):
        QtGui.QMainWindow.__init__(self, win_parent)
        self.create_widgets()

    def create_widgets(self):

        # Menubar function
        # Change path option
        changePath = QtGui.QAction(QtGui.QIcon('img/folder-icon.png'), '&Change folder', self)
        changePath.setShortcut('Ctrl+P')
        changePath.triggered.connect(self.browseDir)
        # Exit option
        exitOption = QtGui.QAction(QtGui.QIcon('img/exit-icon.png'), '&Exit', self)
        exitOption.setShortcut('Ctrl+Q')
        exitOption.triggered.connect(QtGui.qApp.quit)
        # About option
        aboutOption = QtGui.QAction(QtGui.QIcon('img/about-icon.png'), '&About ManGet', self)
        aboutOption.triggered.connect(self.aboutManget)
        # License option
        licenseOption = QtGui.QAction(QtGui.QIcon('img/license-icon.png'), '&ManGet License', self)
        licenseOption.triggered.connect(self.MangetLicense)

        # Setting the menubar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        helpMenu = menubar.addMenu('&Help')
        fileMenu.addAction(changePath)
        fileMenu.addAction(exitOption)
        helpMenu.addAction(aboutOption)
        helpMenu.addAction(licenseOption)

        # Logo image
        pic = QtGui.QPixmap('img/manga-icon.png')

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pic)

        self.label = QtGui.QLabel('MangaReader link:')
        self.linkEdit = QtGui.QLineEdit()
        self.linkButton = QtGui.QPushButton('Download')
        self.pathLabel = QtGui.QLabel('Saving path:')
        self.pathLabel.move(100, 100)
        self.pathEdit = QtGui.QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.path2 = str(self.pathEdit)

        if not self.pathEdit:
            sys.exit(1)

        QtCore.QObject.connect(self.linkButton, QtCore.SIGNAL('clicked()'), self.on_link_clicked)

        # Introductory text
        self.text = u'ManGet v0.2 BETA'
        self.text2 = u'ManGet is a small app that allows you to download manga from'
        self.text3 = u'mangareader.net (more to come). This app is in beta stage and all updates'
        self.text4 = u'will be posted in the official github repository, so stay tuned!'

        grid = QtGui.QGridLayout()
        grid.addWidget(self.label, 1, 0)
        grid.addWidget(self.linkEdit, 1, 1)
        grid.addWidget(self.linkButton, 1, 2)
        grid.addWidget(self.pathLabel, 2, 0)
        grid.addWidget(lbl, 4, 0)

        centralWidget = QtGui.QWidget()
        centralWidget.setLayout(grid)
        self.setCentralWidget(centralWidget)

        self.setGeometry(300, 300, 500, 250) # position-x, position-y, width, height
        self.setWindowTitle('ManGet v0.2 BETA') # Title
        self.setWindowIcon(QtGui.QIcon('img/manga-icon.png')) # Icon

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QtGui.QColor(0, 0, 0))
        qp.setFont(QtGui.QFont('Open Sans', 18))
        qp.drawText(150, 140, self.text)    
        qp.setFont(QtGui.QFont('Droid Sans', 9))
        qp.drawText(150, 160, self.text2)   
        qp.drawText(150, 170, self.text3)
        qp.drawText(150, 180, self.text4)
        qp.drawText(150, 85, self.path2)

    # This is complicated crap
    def browseDir(self):
        dirMessage = QtGui.QMessageBox(self)
        dirMessage.information(self, 'Pending', 'This feature\'s still in development. Sorry for any inconvenience.')

    # My idea and how I will develop it
    def aboutManget(self):
        about = QtGui.QMessageBox(self)
        about.about(self, 'About ManGet', """ManGet is a free, open-source project that allows you to get your manga from your favourite sites. Right now is at beta stage and so many features are not yet implemented and many sites have not been covered yet.

Future features:
    *RSS downloads
    *Better image tagging
    *Auto-update (only for stable branches)

Future sites:
    *Mangafox
    *Batoto
    *ExHentai
    *E-Hentai
    (More to add, just pull a request in the git)

Remember always to check the official git and to update the program as much as you can. Fork, pull requests and issue bugs, that always helps.

Many thanks to:
    *Books authors such as: Learn Python the Hard Way, Python for begginers, Nettuts+, Python Docs, etc.
    *The libraries I've used: BeautifulSoup and PyQt4.
    *4chan, specially /a/ for the idea and /g/ for the feedback.
    *StackOverflow for answering all of my questions.
    *Everyone who works and contributes to Python, a beautiful and excellent language!""")

    # Free as in BSD free
    def MangetLicense(self):
        license = QtGui.QMessageBox(self)
        license.setWindowTitle('ManGet License')
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

    def on_link_clicked(self):
        self.a = self.linkEdit.displayText()
        download_mango2(self.a, self.path2)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = HelloWindow()
    mainWindow.show()
    app.exec_()
