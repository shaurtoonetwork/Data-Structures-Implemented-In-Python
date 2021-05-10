l1 = []
l2 = []

n=5 

def enqueue(data):
    if (len(l1) == n):
        print("Overflow")
        return

    l1.append(data)


def dequeue():
    if(l1 == [] and l2 == []):
        print("Underflow")
        return

    if(l2 == []):
        while not l1 == []:
            l2.append(l1[-1])
            l1.pop()

    l2.pop()



def front():
    if(l1 == [] and l2 == []):
        print("Underflow")
        return

    if(l2 == []):
        while not l1 == []:
            l2.append(l1[-1])
            l1.pop()

    print(l2[-1])


if __name__ == '__main__':
    
    enqueue(1)
    enqueue(2)
    enqueue(3)
    enqueue(4)
    enqueue(5)
    dequeue()
    dequeue()
    dequeue()
    dequeue()
    dequeue()
    dequeue()



    





