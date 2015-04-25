#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vishrut Sutaria
#
# Created:     24/01/2014
# Copyright:   (c) Vishrut Sutaria 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
#Steve
class EntryBox:
    def __init__(self,win,Point1,Point2,Width,Text):
        self.P1 = Point1
        self.P2 = Point2
        self.Width = Width
        self.Point = Point(self.P1,self.P2)
        self.TextBox = Entry((self.Point),self.Width)
        self.TextBox.setFill("White")
        self.TextBox.setText(Text)
        self.TextBox.setTextColor("Gray")
        self.TextBox.setSize(20)
        self.TextBox.draw(win)

    def returnText(self):
        return self.TextBox.getText()

    def setText(self,text):
        self.TextBox.setText(text)
    def setTextColor(self,color):
        self.TextBox.setTextColor(color)
    def UndrawEntry(self):
        self.TextBox.undraw()