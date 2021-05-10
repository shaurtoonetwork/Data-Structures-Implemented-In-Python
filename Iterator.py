def top_ten():
    n=1
    while n<=9:
        sq=n*n
        yield sq    #Generators
        n+=1



values = top_ten()
for i in values:
    print(i)
