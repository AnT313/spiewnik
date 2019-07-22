from song import *
from PySide2.QtWidgets import QPlainTextEdit,QLineEdit,QLabel,QPushButton, QHBoxLayout,  QVBoxLayout, QFormLayout,QWidget
from PySide2.QtCore import QSize, Slot
class Adder(QWidget):
    def __init__(self,songs):
        QWidget.__init__(self)
        self.songs=songs
        self.setMinimumSize(QSize(800, 800))
        self.setWindowTitle('Kwik -- add')
        self.title=QLineEdit(self)
        self.subtitle=QLineEdit(self)
        self.subtitle.move(100,50)
        self.label3=QLabel('Text:',self)
        self.text=QPlainTextEdit(self)
        self.text.setMinimumSize(200,200)
        self.label4=QLabel('Chords:',self)
        self.chords=QPlainTextEdit(self)
        self.chords.setMinimumSize(200,200)
        self.preButton=QPushButton('preview',self)
        self.addButton=QPushButton('add',self)
        self.closeButton=QPushButton('close',self)
        self.browser=QPlainTextEdit(self)
        self.browser.setMinimumSize(200,200)
        self.browser.setReadOnly(True)
        self.connectSlots()
        self.createLayouts()

    def connectSlots(self):
        self.preButton.clicked.connect(self.preview)
        self.addButton.clicked.connect(self.add)
        self.closeButton.clicked.connect(self.close)

    def createLayouts(self):
        l_main=QHBoxLayout()
        l_left=QVBoxLayout()
        l_right=QVBoxLayout()
        l_main.addLayout(l_left)
        l_main.addLayout(l_right)
        l_headers=QFormLayout()
        l_left.addLayout(l_headers)
        l_headers.addRow("&Title:",self.title)
        l_headers.addRow("&Description:",self.subtitle)
        l_left.addWidget(self.label3)
        l_left.addWidget(self.text)
        l_left.addWidget(self.label4)
        l_left.addWidget(self.chords)
        l_right.addWidget(self.browser)
        l_buttons=QHBoxLayout()
        l_right.addLayout(l_buttons)
        l_buttons.addWidget(self.preButton)
        l_buttons.addWidget(self.addButton)
        l_buttons.addWidget(self.closeButton)
        self.setLayout(l_main)

    @Slot()
    def preview(self):
        title=self.title.text()
        subtitle=self.subtitle.text()
        text=self.text.toPlainText().split('\n')
        chords=self.chords.toPlainText().split('\n')
        newSong=song(title,subtitle,text,chords)
        self.browser.setPlainText(newSong.plainText())
        return newSong

    @Slot()
    def add(self):
        self.songs.append(self.preview())
