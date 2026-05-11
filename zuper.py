class Shape :
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self) :
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle (Shape):
    def __init__(self,color,is_filled,radius) :
        self.color = color
        self.is_filled = is_filled
        self.radius = radius
    def describe(self):
        print("This circle got your nuts tied I see !")
        super().describe()
class Square (Shape):
     def __init__(self,color,is_filled,width) :
        self.color = color
        self.is_filled = is_filled
        self.width = width
class Triangle (Shape):
     def __init__(self,color,is_filled,width,height) :
        self.color = color
        self.is_filled = is_filled
        self.width = width
        self.height = height
circle = Circle("red",True,45)
quare = Square("cyan",False,8)

circle.describe()
quare.describe()