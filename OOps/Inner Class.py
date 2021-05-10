class Student:
  
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
   

    def show(self):
        print("Inner")
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "Hp"
            self.cpu = "i5"
            self.ram = 8
    

        def show(self):
            print("Inner Inner")


s1 = Student("Shaurya",7)
s2 = Student("Ayushi",8)

s1.show()


