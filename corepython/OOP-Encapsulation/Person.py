# from datetime import datetime
# from tkinter.font import names
#
#
# class Person:
#     AVG_AGE = 18  # static constant
#
#     def __init__(self):
#         print(" Cons is calling  the person class")
#         self.__name = None
#         self.__dob = None
#         self.__address = None
#
#     # Getter and Setter for name
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     # Getter and Setter for dob
#     def get_dob(self):
#         return self.__dob
#
#     def set_dob(self, dob):
#         self.__dob = dob  # dob should be datetime object
#
#     # Getter and Setter for address
#     def get_address(self):
#         return self.__address
#
#     def set_address(self, address):
#         self.__address = address
#
#
# p = Person()
# p.set_name("rohan")
# p.set_address("Indore")
# p.set_dob(datetime(2000, 5, 15))
#
# print("Name:", p.get_name())
# print(p.get_dob())
# print(Person.AVG_AGE)

from datetime import datetime

class Person:
    AVG_AGE = 18

    def __int__(self):
        self.__name = None
        self.__dob = None
        self.__address = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


    def get_dob(self):
        return self.__dob

    def set_dob(self , dob):
        self.__dob = dob


    def get_address(self):
        return self.__address

    def set_address(self , address):
        self.__address = address


p = Person()
p.set_name("Rohan")
p.set_address("Indore")
p.set_dob(datetime(2004,5,8))

print("name:",p.get_name())
print(p.get_dob())
print(Person.AVG_AGE)




























