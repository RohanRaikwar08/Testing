class Shape():
    def area(self):
        print("Shape area....")
        return print("shape class area method")


class rectangle(Shape):
    def area(self):
        print("rectangle area...")
        return print("rectangle class area method")

s = Shape()
s.area()

r = rectangle()
r.area()

shape: Shape = rectangle()
shape.area()


