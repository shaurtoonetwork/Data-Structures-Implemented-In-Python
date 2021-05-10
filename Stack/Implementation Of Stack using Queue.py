q1 = []
q2 = []

n = 5

def push(data):

    if not q1==[] and len(q1) == n:
        print("Overflow")
        return

    if not q2==[] and len(q2) == n:
        print("Overflow")
        return

    if(q2 == []):
        q1.append(data)
    else:
        q2.append(data)



def pop():

    if(q1 == [] and q2 == []):
        print("Underflow")

    if(not q1 == []):
        while(len(q1)>1):
            q2.append(q1[0])
            q1.pop(0)

        q1.pop()
        return    

    if(not q2 == []):
        while(len(q2)>1):
            q1.append(q2[0])
            q2.pop(0)

        q2.pop()
        return


def Top():

    if(q1 == [] and q2 == []):
        print("Underflow")

    if(not q1 == []):
        while(len(q1)>1):
            q2.append(q1[0])
            q1.pop(0)

        x = q1[0]
        q1.pop(0)
        q2.append(x)
        return x

    if(not q2 == []):
        while(len(q2)>1):
            q1.append(q2[0])
            q2.pop(0)

        x = q2[0]
        q2.pop(0)
        q1.append(x)
        return x


if __name__ == '__main__':
    push(1)
    push(2)
    push(3)
    push(4)
    push(5)
    print(q1)
    print(q2)
    pop()
    print(q1)
    print(q2)
    print(Top())
 







