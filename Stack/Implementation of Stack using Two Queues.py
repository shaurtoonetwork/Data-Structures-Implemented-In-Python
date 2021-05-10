from queue import Queue

q1=Queue()
q2=Queue()

n=5

def push(data):
    if(not q1==[] and q1.size()==n):
        print("Overflow")
        return

    if(not q2==[] and q2.size()==n):
        print("Overflow")
        return

    if(q2.is_empty()):
        q1.enqueue(data)
    else:
        q2.enqueue(data)


def pop():
    if(q1==[] and q2==[]):
        print("Underflow")
        return

    if(not q1==[]):
        while(q1.size()>1):
            q2.enqueue(q1.frontvalue())
            q1.dequeue()
        q1.dequeue()
        return

    if(not q2==[]):
        while(q2.size()>1):
            q1.enqueue(q2.frontvalue())
            q2.dequeue()
        q2.dequeue()
        return


    
def Top():
    if(q1==[] and q2==[]):
        print("Underflow")

    if(not q1==[]):
        while(q1.size()>1):
            q2.enqueue(q1.frontvalue())
            q1.dequeue()

        x=q1.frontvalue()
        q1.dequeue()
        q2.enqueue(x)
        return x
    return

    if(not q2==[]):
        while(q2.size()>1):
            q1.enqueue(q2.frontvalue())
            q2.dequeue()

        x=q2.frontvalue()
        q2.dequeue()
        q1.enqueue(x)
        return x
    return



if __name__ == '__main__':
    push(2)
    push(3)
    push(4)
    push(5)
    push(6)
    q1.get_queue()
    q2.get_queue()
    pop()
    q1.get_queue()
    q2.get_queue()





