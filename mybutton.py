#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vishrut Sutaria
#
# Created:     23/01/2014
# Copyright:   (c) Vishrut Sutaria 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
class MyButton:
    """Creates a button by making a labeled rectangle.
    The click method will return True/False depending if the click point
    is inside or not. The getLabel method returns the text in the rectangle."""
    def __init__(self,win,x1,x2,y1,y2,Label,Fill,TextColour):
        self.win = win
        self.x1,self.x2,self.y1,self.y2 = x1,x2,y1,y2
        self.Button = Rectangle(Point(self.x1,self.y1),Point(self.x2,self.y2))
        self.Button.setFill(Fill)
        self.Button.draw(win)
        self.Label = Text(Point(((self.x1+self.x2)/2),((self.y1+self.y2)/2)),Label)
        self.Label.setFill(TextColour)
        self.Label.draw(win)

    def click(self,pt):
        #Returns True/False depending if the pt is inside the rectangle
        return pt.getX() >= self.x1 and pt.getX() <= self.x2 and pt.getY() >= self.y1 and pt.getY() <= self.y2

    def getLabel(self):
        #Returns the label of the rectangle
        return self.Label.getText()

    def UndrawButton(self):
        self.Button.undraw()
        self.Label.undraw()