from graphics import*
from objects import*
#Steve Truong
class CreateRectangle(Objects):
    """Subclass of the class Objects. Takes all the methods and functions that Object class has.
    Creates a rectangle will colour/text. Has a Draw() method that draws the rectangle
    and an Undraw() method that undraws the rectangle."""
    def Draw(self):
        #Draws the rectangle and the label
        self.Rect = Rectangle(Point(self.x1,self.y1),Point(self.x2,self.y2))
        self.Rect.setFill("dodgerblue")
        self.Rect.draw(self.win)

        self.Label = Text(Point(((self.x1+self.x2)/2),((self.y1+self.y2)/2)),self.Text)
        self.Label.setFill('white')
        self.Label.draw(self.win)


    def Undraw(self):
        #Undraws the rectangle and the label
        self.Rect.undraw()
        self.Label.undraw()