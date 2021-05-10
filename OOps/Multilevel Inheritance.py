#Mutilevel Level Inheritance
# A->B->C

class A: #Super Class or Parent Class
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")


class B(A): # Subclass or Child Class
    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")

class C(B):   #GrandChild class
    def feature5(self):
        print("Feature 5 Working")


c1 = C()

c1.feature3()
c1.feature1()


