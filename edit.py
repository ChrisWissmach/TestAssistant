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
from studentclass import  *
class Edit(Student):
      def ChangeInfo(self,NewPass1,NewPass2):
          """This just assigns instance variables for the new password."""
          self.NewPass1 = NewPass1
          self.NewPass2 = NewPass2
      def ChangePass(self):
          """This just checks if the old and new are same or not. If
                  they are sane no need in changing the password, if not
                  the same then password is changed."""
          print(self.NewPass1)
          print(self.Pass1,"Before check")
          if self.NewPass1 == self.Pass1:
             pass
          else:
               self.Pass1,self.Pass2 = self.NewPass1,self.NewPass1
          print(self.Pass1,"after check")
          return