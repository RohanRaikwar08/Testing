class Shape:
    def execute(self):
        print("Shape execute method")
        self.area()

    def area(self):
        print("Shape area method")


class rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rectangle_area = self.length * self.width
        print("rectangle area:", rectangle_area)
        return rectangle_area


class Circle(Shape):
    PI = 3.14

    def __inti__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = self.PI * self.radius * self.radius
        print("Circle area:", circle_area)
        return circle_area



class Test(Shape):
    pass


r = rectangle(10, 20)
r.execute()


c = Circle(10)
c.execute()

t = Test()
t.execute()
