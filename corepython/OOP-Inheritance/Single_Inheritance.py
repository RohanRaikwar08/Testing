# class Shape:
#     def __init__(self):
#         self.colour = ''
#         self.borderWidth = 0
#
#     def get_colour(self):
#         return self.colour
#
#     def set_colour(self,colour):
#         self.colour = colour
#
#     def get_borderWidth(self):
#         return self.borderWidth
#
#     def set_borderWidth(self,borderWidth):
#         self.borderWidth = borderWidth
#
#
# class Rectangle(Shape):
#     def __init__(self):
#         self.length = 0
#         self.breathe = 0
#
#     def get_length(self):
#         return self.length
#
#     def set_length(self,length):
#         self.length = length
#
#     def get_breathe(self):
#         return self.breathe
#
#     def set_breathe(self,breathe):
#         self.breathe = breathe
#
#
# r = Rectangle()
# r.set_length(10)
# r.set_breathe(20)
# r.set_colour("Blue")
# r.set_borderWidth(500)
#
# print("length:",r.get_length())
# print("breathe:",r.get_breathe())
# print("colour:",r.get_colour())
# print("borderWidth:",r.get_borderWidth())

# class RBI:
#     def __init__(self):
#         self.saving = 0
#         self.current = 0
#
#     def get_saving(self):
#         return self.saving
#
#     def set_saving(self,saving):
#         self.saving = saving
#
#     def get_current(self):
#         return self.current
#
#     def set_current(self,current):
#         self.current = current
#
# class Central(RBI):
#     def __init__(self):
#         self.deposit = 0
#         self.loan = 0
#
#     def get_deposit(self):
#         return self.deposit
#
#     def set_deposit(self,deposit):
#         self.deposit = deposit
#
#     def get_loan(self):
#         return self.loan
#
#     def set_loan(self,loan):
#         self.loan = loan
#
# c = Central()
# c.set_deposit(600)
# c.set_loan(1000)
# c.set_saving(500)
# c.set_current(200)
#
# print("deposit:",c.get_deposit())
# print("loan:",c.get_loan())
# print("saving:",c.get_saving())
# print("current:",c.get_current())



class School:
    def __init__(self):
        self.principal = ''
        self.student = 0

    def get_principal(self):
        return self.principal

    def set_principal(self,principal):
        self.principal = principal

    def get_student(self):
        return self.student

    def set_student(self,student):
        self.student = student

class Collage(School):
    def __init__(self):
        self.mam = 0
        self.sir = 0

    def get_mam(self):
        return self.mam

    def set_mam(self,mam):
        self.mam = mam

    def get_sir(self):
        return self.sir

    def set_sir(self,sir):
        self.sir = sir


c = Collage()
c.set_mam(20)
c.set_sir(25)
c.set_principal(1)
c.set_student(5000)


print("mam:",c.get_mam())
print("sir:",c.get_sir())
print("principal:",c.get_principal())
print("student:",c.get_student())























