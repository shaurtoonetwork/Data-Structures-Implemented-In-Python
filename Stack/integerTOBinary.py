from Stack import Stack

"""
242 / 2 = 121 ->    0
121 / 2 = 60 ->     1
60 / 2 = 30 ->      0
30 / 2 = 15 ->      0
15 / 2 = 7 ->       1
7 / 2 = 3->         1
3 / 2 = 1 ->        1
1 / 2 = 0 ->        1
Integer To Binary ->   11110010
"""

def intToBinary(dec_num):
    s=Stack()
    count = 0
    while dec_num>0:
        r=dec_num%2
        s.push(r)
        dec_num = dec_num//2
        if r==1:
            count+=1

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    print(count)
    print(bin_num)

intToBinary(12)

        


