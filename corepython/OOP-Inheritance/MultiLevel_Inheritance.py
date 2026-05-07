class Student:
    def getstudent(self):
        self.name = input("Name:")
        self.age = input("Age:")
        self.Gender = input("Gender:")


class Test(Student):
    def getmarks(self):
        self.studentclass = input("Class:")
        print("Enter the marks of the represtative marks")
        self.english = int(input("English:"))
        self.hindi = int(input("Hindi:"))
        self.maths = int(input("Maths:"))
        self.physics = int(input("Physics:"))


class Marks(Test):
    def display(self):
        print("n\nName:", self.name)
        print("Age:",self.age)
        print("Gender:",self.Gender)
        print("Class:",self.studentclass)
        print("english:",self.english)
        print("hindi:",self.hindi)
        print("maths:",self.maths)
        print("physics:",self.physics)
        total_marks = self.english + self.hindi + self.maths + self.physics
        if total_marks > 100:
            print("Passed")

        else:
            print("Failed")
        print("Total Marks:",total_marks)


m = Marks()
m.getstudent()
m.getmarks()
m.display()



