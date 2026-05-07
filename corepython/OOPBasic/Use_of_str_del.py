class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __del__(self):
        ClassName = self.__class__.__age__
        print("Destroying", ClassName)


    def __str__(self):
        return "person: name = %s , age = %s " % ( self.name, self.age)


























