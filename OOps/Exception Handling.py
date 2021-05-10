a = 5
b = 2


try:
    print("Resource Opened")
    print(a/b)
    p = int(input("Enter a Number"))
    print(p)
except Exception as e:
    print(e)

finally:
    print("Resource Closed")