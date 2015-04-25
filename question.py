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
from entrybox import*
from graphics import*
#Jimmy
class Question:
    def __init__(self,win):
        self.win=win
    #Creates the Entry Boxes
    def TestBoxes(self):
    #Teachers Puts in the Question, Correct Answer, and 3 Wrong Answers
        self.QuestionBox = EntryBox(self.win,300,100,30,"Question")
        self.CorrectBox = EntryBox(self.win,300,150,30,"Correct Answer")
        self.WrongBox1 = EntryBox(self.win,300,200,30,"Wrong Answer 1")
        self.WrongBox2 = EntryBox(self.win,300,250,30,"Wrong Answer 2")
        self.WrongBox3 = EntryBox(self.win,300,300,30,"Wrong Answer 3")

    def getQuestion(self):
        return self.QuestionBox.returnText()
    def getCorrectAnswer(self):
        return self.CorrectBox.returnText()
    def getWrongAnswers(self):
        return self.WrongBox1.returnText(),self.WrongBox2.returnText(),self.WrongBox3.returnText()