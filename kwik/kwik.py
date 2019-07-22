#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import sys
import os
import song
import pickle
from adderwidget import *
from PySide2.QtWidgets import QApplication, QListWidget

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumSize(QSize(800, 800))
        self.setWindowTitle('Kwik')
        self.filename="songs.db"
        if(os.path.isfile(self.filename) and os.path.getsize(self.filename) > 0):
            file=open(self.filename,"rb")
            self.songs=pickle.load(file)
            file.close()
        else:
            self.songs=[]
        self.slist=QListWidget(self)
        for i in self.songs:
            self.slist.addItem(i.title)
        self.adderButton=QPushButton("add new",self)
        self.saveButton=QPushButton("save",self)
        self.browser=QPlainTextEdit(self)
        self.browser.setMinimumSize(200,200)
        self.browser.setReadOnly(True)
        self.connectSignals()
        self.createLayouts()


    def connectSignals(self):
        self.adderButton.clicked.connect(self.startAdding)
        self.saveButton.clicked.connect(self.save)
        self.slist.currentRowChanged.connect(self.viewSong)

    def createLayouts(self):
        l_main=QHBoxLayout()
        l_left=QVBoxLayout()
        l_left.addWidget(self.slist)
        l_buttons=QHBoxLayout()
        l_left.addLayout(l_buttons)
        l_buttons.addWidget(self.adderButton)
        l_buttons.addWidget(self.saveButton)
        l_right=QVBoxLayout()
        l_main.addLayout(l_left)
        l_main.addLayout(l_right)
        l_right.addWidget(self.browser)
        self.setLayout(l_main)

    @Slot()
    def startAdding(self):
        self.adder=Adder(self.songs)
        self.adder.addButton.clicked.connect(self.appendlist)
        self.adder.show()


    @Slot()
    def save(self):
        file=open(self.filename,"wb")
        pickle.dump(self.songs,file)
        file.close()

    @Slot()
    def viewSong(self,i):
        self.browser.setPlainText(self.songs[i].plainText())

    @Slot()
    def appendlist(self):
        self.slist.addItem(self.songs[-1].title)



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
