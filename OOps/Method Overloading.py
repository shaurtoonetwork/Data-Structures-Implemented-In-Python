#Method Overloading In Python
class Student:
    def sum(self,*num):
        s = 0
        for n in num:
            s = s + n
        return s


s= Student()

print(s.sum(2,2,2))