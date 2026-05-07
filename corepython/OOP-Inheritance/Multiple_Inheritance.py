class Addition:
    def sum(self,a,b):
        return a + b

class Multiplication:
    def multiply(self,a,b):
        return a * b

class Derived(Addition,Multiplication):
    def Divide(self,a,b):
        return a / b


derived_obj = Derived()
print(derived_obj.sum(10,10))
print(derived_obj.multiply(10,10))
print(derived_obj.Divide(10,10))


class subtraction:
    def subtract(self,a,b):
        return a - b

class addtition:
    def add(self,a,b):
        return a + b

class Derived(subtraction,addtition):
    def multiply(self,a,b):
        return a * b


derived_obj = Derived()
print(derived_obj.subtract(20,10))
print(derived_obj.add(20,10))
print(derived_obj.multiply(20,10))



























