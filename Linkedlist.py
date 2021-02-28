class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
        
    #Function to Print the List

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
            
     #Append Function to Insert the Node at the END of the LinkedList
            
    def append(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
        
    #Prepend Function To add Node at the Beginning of The Linked List

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

        
     
    #Function to add Node after any Node.
    
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
