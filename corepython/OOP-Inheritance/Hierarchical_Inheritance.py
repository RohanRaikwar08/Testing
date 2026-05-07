# from time import sleep
#
#
# class shape:
#     def __init__(self,colour = '',borderWidth = 0):
#         self.colour = colour
#         self.borderWidth = borderWidth
#
#     def get_colour(self):
#         return self.colour
# a
#     def set_colour(self,colour):
#         self.colour = colour
#
#     def get_borderWidth(self):
#         return self.borderWidth
#
#     def set_borderWidth(self,borderWidth):
#         self.borderWidth = borderWidth
#
# class Rectangle(shape):
#     def __init__(self,length= 0,width = 0,colour ='',borderWidth=0 ):
#         self.length = length
#         self.width = width
#         super().__init__(colour,borderWidth)
#
#     def get_length(self):
#         return self.length
#
#     def set_length(self,length):
#         self.length = length
#
#     def get_width(self):
#         return self.width
#
#     def set_width(self,width):
#         self.width = width
#
# class Circle(shape):
#     def __init__(self,radius=0,colour='',borderWidth= 0):
#         self.radius = radius
#         super().__init__(colour,borderWidth)
#
#     def get_radius(self):
#         return self.radius
#
#     def set_radius(self,radius):
#         self.radius = radius
#
# r = Rectangle(10,20,"black",100)
# print("Rectangle:")
# print("length:",r.get_length())
# print("width:",r.get_width())
# print("colour:",r.get_colour())
# print("borderWidth:",r.get_borderWidth())
#
#
# c = Circle(12,"blue",50)
# print("\nCircle:")
# print("Radius:",c.get_radius())
# print("colour:",c.get_colour())
# print("borderWidth:",c.get_borderWidth())

class Central:
    def __init__(self,loan = 0,intrest= ''):
        self.loan = loan
        self.intrest = intrest

    def get_loan(self):
        return self.loan

    def set_loan(self,loan):
        self.loan = loan

    def get_intrest(self):
        return self.intrest

    def set_intrest(self,intrest):
        self.intrest = intrest

class Rbi(Central):
    def __init__(self,saving= 0,current = 0,loan = 0 ,intrest= ''):
        self.saving = saving
        self.current = current
        super().__init__(loan,intrest)


    def get_saving(self):
        return self.saving

    def set_saving(self,saving):
        self.saving = saving

    def get_current(self):
        return self.current

    def set_current(self,current):
        self.current = current


class Kotak(Central):
    def __init__(self,withdrwal=0,loan =0,intrest=''):
        self.withdrawl  = withdrwal
        super().__init__(loan,intrest)

    def get_withdrawl(self):
        return self.withdrawl

    def set_withdrawl(self,withdrawl):
        self.withdrwal = withdrawl


r = Rbi(5000,600,10000,12)
print("Rbi:")
print("loan:",r.get_loan())
print("intrest:",r.get_intrest())
print("saving:",r.get_saving())
print("current:",r.get_current())


k = Kotak(2000,20000,15)
print("\nKotak:")
print("withdrawl:",k.get_withdrawl())
print("loan:",k.get_loan())
print("intrest:",k.get_intrest())




















