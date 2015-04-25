#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Anyone
#
# Created:     04/11/2013
# Copyright:   (c) Anyone 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
class circlebutton:
      def __init__(self,win,center,width,label,colour,textcolour):
          """ Creates a circular button, eg:
              qb = Button(myWin,centerpoint,width,height,'quit')"""
          x,y = center.getX(), center.getY()

          radius= width/2.0

          self.xmax, self.xmin = x+radius,x-radius
          self.ymax, self.ymin = y+radius,y-radius

          p1 = Point(self.xmin,self.ymin)
          p2 = Point(self.xmax,self.ymax)

          self.circle = Circle(center,radius)
          self.circle.setFill(colour)

          self.label = Text(center,label)
          self.label.setFill(textcolour)

          self.deactivate()

      def clicked(self,p):
          "Returns true if the button active and p is inside"

          return(self.active and
                 self.xmin <= p.getX() <= self.xmax and
                 self.ymin <= p.getY() <= self.ymax)
      def activate(self,win):
          "Sets this button to 'active'."
          self.circle.draw(win)
          self.label.draw(win)
          self.active = True

      def deactivate(self):
          "Sets this button to 'inactive'."
          "This helps to undraw objects that are not needed"
          "on the graphics window at a certain "
          self.label.undraw()
          self.circle.undraw()
          self.active = False

