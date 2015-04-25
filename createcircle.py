from graphics import*
from objects import*
#Steve Truong
class CreateCircle(Objects):
    """Subclass of the class Objects. Takes all the methods and functions that Object class has.
    Creates a circle will colour/text. Has a Draw() method that draws the triangleand an Undraw()
    method that undraws the triangle. The Unshow() will make the circle white with a white outline
    and the Show() method will make set the circle to the fill colour chosen - used to show/unshow
    the dots/points."""
    def Draw(self):
        #Draws the circle
        self.Cir = Circle(self.center,self.width)
        self.Cir.setFill('white')
        self.Cir.draw(self.win)

        self.Label = Text(self.center, self.Text)
        self.Label.draw(self.win)

    def Undraw(self):
        #Undraws the circle and the label
        self.Cir.undraw()
        self.Label.undraw()

    def Unshow(self):
        #Sets the circle to white
        self.Cir.setFill("white")
        self.Cir.setOutline("white")

    def Show(self):
        #Sets the circel to black
        self.Cir.setFill(self.Fill)