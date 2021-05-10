class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):      #We have changed the add operator, We have overloaded the add operator to add two Class objects.
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self,other):     #We have changed the greater than operator, We have overloaded the greater than operator to compare two Class objects.
        m1 = self.m1+other.m1
        r1 = self.m1+self.m2
        r2 = other.m1+other.m2

        if r1>r2:
            return True
        else:
            return False

    def __str__(self):
        return "{} {}".format(self.m1,self.m2)


  


s1=Student(2,3)
s2=Student(4,5)

s3  = s1+s2
print(s3.m1,s3.m2)

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s1.__str__())