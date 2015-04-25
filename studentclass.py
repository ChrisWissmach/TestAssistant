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
class Student:
    def __init__(self,win,Name,Last,User,Pass1,Pass2):
        self.Name = Name
        self.Last = Last
        self.User = User
        self.Pass1 = Pass1
        self.Pass2 = Pass2
    def FullName(self):
        return self.Name,self.Last
    def Username(self):
        return self.User