class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Debugging")

class Laptop:
    def code(self,ide):
        ide.execute()


ide = MyEditor() # or Ide=PyCharm()
#If this Object has the method execute(), Thats it, we are not concerned about which class method it is.

l = Laptop()
l.code(ide)


#Duck Tying is a Type System used in Dynamic Languages. For Example - Python, Pearl, Javascript, Ruby.
#In Duck Typing the type or the class of an Object is less important than the method it defines.
# In Duck typing we do not check types at all. Instead, we check for the prescence of given method or attribute. 
#If a Bird Behaves like a Duck, It quacks like a Duck, It is a Duck.