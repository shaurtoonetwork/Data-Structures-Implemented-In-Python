#Using classname.method
'''class Parent:
    def show(self):
        print("Inside Parent")

class Child(Parent):
    def show(self):
        Parent.show(self)
        print("Inside Child")

O = Child()
O.show()'''

#Using super()
class Parent:
    def show(self):
        print("Inside Parent")

class Child(Parent):
    def show(self):
        super().show()
        print("Inside Child")

O = Child()
O.show()
