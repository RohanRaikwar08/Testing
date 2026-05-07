# class Automobile:
#
#     NO_OF_GEARS = 6
#
#     def __init__(self):
#         self.__colour = None
#         self.__speed = 0
#         self.__make = None
#
#
#     def get_colour(self):
#         return self.__colour
#
#     def set_colour(self,colour):
#         self.__colour =  colour
#
#     def get_speed(self):
#         return self.__speed
#
#     def set_speed(self,speed):
#         self.__speed = speed
#
#     def get_make(self):
#         return self.__make
#
#     def set_make(self,make):
#         self.__make = make
#
#
# car = Automobile()
# car.set_colour("Red")
# car.set_make("BMW")
# car.set_speed(500)

class Automobile:

    NO_OF_GEARS = 6

    def __init__(self):
        self.__colour = None
        self.__speed = 0
        self.__make = None

    def get_colour(self):
        return self.__colour

    def set_colour(self,colour):
        self.__colour = colour

    def get_speed(self):
        return self.__speed

    def set_speed(self,speed):
        self.__speed = speed

    def get_make(self):
        return self.__make

    def set_make(self,make):
        self.__make = make

car = Automobile()
car.set_colour("Blue")
car.set_make("OD")
car.set_speed(450)



























