def IntToBin(DN):
    s = []
    count = 0
    while DN>0 :
        r = DN % 2
        s.append(r)
        if r==1:
            count+=1
        DN = DN//2

    print(count)

    BN = ""
    while not s == []:
        BN+=str(s.pop())
    
    return(BN)


print(IntToBin(3))