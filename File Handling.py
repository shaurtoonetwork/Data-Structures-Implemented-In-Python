f = open('mydata.txt', 'r')


f1 = open('abc.txt','w')
f1.write("")


for data in f:
    f1.write(data)

