
#creates a rect object
class Rectangle:
  #constructor that sets a pos (x, y) and height and width
  def __init__(self, x=0, y=0, h=0, w=0):
    self.x = 0 if x < 0 else x
    self.y = 0 if y < 0 else y
    self.height = 0 if h < 0 else h
    self.width = 0 if w < 0 else w

  #returns the values of the rect fields as a string
  def __str__(self):
    return f"(x:{self.x}, y:{self.y}) height: {self.height}, width: {self.width}"