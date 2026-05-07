class Shape:
    def __init__(self,colour,borderWidth):
        self.colour = colour
        self.borderWidth = borderWidth

    def get_colour(self):
        return self.colour

    def set_colour(self,colour):
        self.colour = colour

    def get_borderWidth(self):
        return self.borderWidth

    def set_borderWidth(self,borderWidth):
        self.boderWidth = borderWidth

s = Shape("red",10)
print("Colour:",s.get_colour())
print("borderWidth:",s.get_borderWidth())