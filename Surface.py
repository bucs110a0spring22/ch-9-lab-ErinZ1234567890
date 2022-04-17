from Rectangle import Rectangle
#creates a surface obj that contains a rect & image
class Surface:
  #surface constructor. takes in image filename, pos (x,y), height, & width
  def __init__(self, filename="", x=0, y=0, h=0, w=0):
    self.image = filename
    self.rect = Rectangle(x,y,h,w)
  #getter method for the rect object
  def getRect(self):
    return self.rect