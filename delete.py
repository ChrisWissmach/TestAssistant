#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dongj0497
#
# Created:     23/01/2014
# Copyright:   (c) dongj0497 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os

class DeleteFiles:
      def __init__(self,file):
          self.File = file
      def DeleteFile(self):

        ## if file exists, delete it ##
        if os.path.isfile(self.File):
                os.remove(self.File)
        return