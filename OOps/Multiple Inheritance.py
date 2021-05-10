#Multiple Inheritance
# A  B
#  ||
#  C
class A: #Super Class or Parent Class

    def __init__(self):
        print("A")

    def feature1(self):
        print("Feature 1-A Working")

    def feature2(self):
        print("Feature 2 Working")


class B: # Subclass or Child Class

    def __init__(self):
        print("B")

    def feature1(self):
        print("Feature 1-B Working")

    def feature4(self):
        print("Feature 4 Working")

class C(A,B):   #GrandChild class

    def __init__(self):
        super().__init__()
        print("C")

    def feature5(self):
        print("Feature 5 Working")


c1 = C()
c1.feature1()






