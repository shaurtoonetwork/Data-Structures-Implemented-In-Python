#Single Level Inheritance
# A->B

class A: #Super Class or Parent Class

    def __init__(self):    #Contructor Creation of class A
        print("A")

    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")


class B(A): # Subclass or Child Class

    def __init__(self):  
        super().__init__()  
        print("B")

    def feature3(self):
        print("Feature 1 Working")

    def feature4(self):
        print("Feature 2 Working")


b = B()

