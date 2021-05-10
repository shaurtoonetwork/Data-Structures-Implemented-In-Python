class Person:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    
    def show(self):
        print(self.name,self.rollno)


s1 = Person('Ayushi',2)
s2 = Person('Shaurya',3)

s1.name = "DOn"

s1.show()

