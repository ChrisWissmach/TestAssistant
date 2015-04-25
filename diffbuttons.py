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
from mybutton import *

#Chris (Using inheritance)
class ExitButton(MyButton):
    def Quit(self):
        self.win.close()
        sys.exit()

#Jimmy (Using inheritance)
class InvisibleButton(MyButton):
    def __init__(self,win,x1,x2,y1,y2,Label,Fill,TextColour):
        """Creates the button"""
        self.win = win
        self.x1,self.x2,self.y1,self.y2 = x1,x2,y1,y2
        self.Button = Rectangle(Point(self.x1,self.y1),Point(self.x2,self.y2))
        self.Button.setFill(Fill)
        self.Label = Text(Point(((self.x1+self.x2)/2),((self.y1+self.y2)/2)),Label)
        self.Label.setFill(TextColour)