class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def size(self):
        count=0
        cur_node=self.head

        while cur_node:
            count+=1
            cur_node=cur_node.next

        return count 

    def dequeue(self):
        if self.head is None:
            print("The queue is empty")
        cur_node = self.head
        self.head = cur_node.next
        cur_node  = None

    def get_queue(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next

    def is_empty(self):
        if self.head is None:
            print("Yes")
        else:
            print("No")


    def frontvalue(self):
        if self.head is not None:
            print(self.head.data)
        





q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.get_queue()
q.frontvalue()