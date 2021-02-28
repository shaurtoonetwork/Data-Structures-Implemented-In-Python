class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def append(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def Insert_In_Middle(self,prev_node,data):
        if not prev_node:
            print("Previous Node not in the List")
            return
        
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node

        

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.Insert_In_Middle(llist.head.next,"K")
llist.print_list()
