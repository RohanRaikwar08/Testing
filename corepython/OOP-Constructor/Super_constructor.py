from copyreg import constructor


class shape:
    def __init__(self,colour,borderWidth):
        print("shape constructor called")
        self.colour = colour
        self.borderWidth = borderWidth

    def get_colour(self):
        return self.colour

    def set_colour(self,colour):
        self.colour = colour

    def get_borderWidth(self):
        return self.borderWidth

    def set_borderWidth(self,borderWidth):
        self.borderWidth = borderWidth


class Rectangle(shape):
    def __init__(self, length=0,width = 0 ,colour='',borderWidth = 0):
       self.length = length
       self.width = width
       super().__init__(colour,borderWidth)

    def get_length(self):
        return self.length

    def set_length(self,length):
        self.length= length

    def get_width(self):
        return self.width

    def set_width(self,width):
        self.width = width

r = Rectangle(10,20,"blue",100)
print("Rectangle:")
print("length:",r.get_length())
print("width:",r.get_width())
print("colour:",r.get_colour())
print("borderWidth:",r.get_borderWidth)

