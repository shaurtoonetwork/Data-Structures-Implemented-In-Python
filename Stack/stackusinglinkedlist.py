class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack():
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def pop(self):
        cur_node=self.head
        self.head=cur_node.next
        cur_node=None

    def get_stack(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def peak(self):
        top_node=self.head
        print(top_node.data)

    def size(self,node):
        if node is None:
            return 0
        return 1+self.size(node.next)


    def is_empty(self):
        if self.head is None:
            print("Yes")
        else:
            print("No")





s=Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
s.push("E")
s.pop()
s.pop()
s.get_stack()




