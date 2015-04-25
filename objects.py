from graphics import*
#Steve Truong
class Objects:
    """ The super class program that takes in the coordinates, size, colour, window, and the text.
    The object class has a method called Draw() that has a pass statement"""
    def __init__(self,win,x1,x2,y1,y2,width,Label,Fill):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.Text = Label
        self.center = Point(((self.x1+self.x2)/2),((self.y1+self.y2)/2))
        self.win = win
        self.width = width
        self.Fill = Fill

    def Draw(self):
        pass
