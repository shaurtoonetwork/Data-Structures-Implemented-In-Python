

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

class C(A):   #GrandChild class
    def feature5(self):
        print("Feature 5 Working")

class D(B,C):   #GrandChild class
    def feature6(self):
        print("Feature 6 Working")


b = B()
c = C()
d = D()


