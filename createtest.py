#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Chris
#
# Created:     26/01/2014
# Copyright:   (c) Chris 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from graphics import*
from mybutton import*
from entrybox import*

class CreateTest:
    def __init__(self,win):
        self.win = win

#Creates the Test Buttons
    def TestButtons(self):
        self.CreateTestList = [(0,175,525,600,"Add a New Question", "dodgerblue","White"),(425,600,525,600,"Done Creating Test","dodgerblue","white")]
        self.CreateTestButts = []
        for (x1,x2,y1,y2,label,colour,textcolour) in self.CreateTestList:
            self.CreateTestButts.append(MyButton(self.win,x1,x2,y1,y2,label,colour,textcolour))
        self.ButtonLabel,self.win = GetKeyPress(self.CreateTestButts,self.win)
        return self.ButtonLabel

#Gets the Test Title
    def GetTestName(self):
        #Entry Box for Test Name
        self.TestName = EntryBox(self.win,300,50,30,"Test Name")

        #Creates the Done Button (Finish creating Test Name)
        self.DoneButtonList = [(100,500,125,225,"Done Creating Test Name","Dodgerblue","white")]
        self.ButtonList = []
        for (x1,x2,y1,y2,label,colour,textcolour) in self.DoneButtonList:
            self.ButtonList.append(MyButton(self.win,x1,x2,y1,y2,label,colour,textcolour))
        self.ButtonList.append(MyButton(self.win,0,600,550,600,"Cancel","dodgerblue","white"))
        self.ButtonLabel,self.win = GetKeyPress(self.ButtonList,self.win)
        return self.ButtonLabel,self.ButtonList,self.TestName

def GetKeyPress(ButtonList,win):
    """This function ask the users for a click and figures out if any of the
    buttons were clicked and if they were the loop will find the name of
    the button and return it"""
    while True:
          pt = win.getMouse()
          for Button in ButtonList:
              if Button.click(pt):
                 ButtonLabel = Button.getLabel()
                 print(ButtonLabel)
                 return ButtonLabel,win
              else:
                pass