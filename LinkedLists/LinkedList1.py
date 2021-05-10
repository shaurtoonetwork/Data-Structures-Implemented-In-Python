class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return

        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node 

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def add_after_node(self,prev_node,data):
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def delete_node(self,key):
        cur_node=self.head
        if cur_node and cur_node.data==key:
            self.head=cur_node.next
            cur_node=None

        prev=None
        while cur_node and cur_node.data!=key:
            prev=cur_node
            cur_node=cur_node.next

        if cur_node is None:
            return

        prev.next=cur_node.next
        cur_node = None

    def delete_node_pos(self,pos):
        cur_node = self.head
        if pos==0:
            self.head  = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev  = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next=cur_node.next
        cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count+=1
            cur_node = cur_node.next
        print(count)

    def len_recursive(self,node):
        if node is None:
            return 0
        return 1+self.len_recursive(node.next)

    def swap_nodes(self,node1,node2):
        if node1 == node2:
            return 

        prev1=None
        cur1=self.head
        while cur1 and cur1.data!=node1:
            prev1=cur1
            cur1=cur1.next

        prev2=None
        cur2=self.head
        while cur2 and cur2.data!=node2:
            prev2=cur2
            cur2=cur2.next

        if not cur1 or not cur1:
            return

        if prev1:
            prev1.next=cur2
        else:
            self.head=cur2

        if prev2:
            prev2.next=cur1
        else:
            self.head=cur1

        cur1.next,cur2.next=cur2.next,cur1.next



llist=Linkedlist()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.swap_nodes("B","C")
llist.printlist()
