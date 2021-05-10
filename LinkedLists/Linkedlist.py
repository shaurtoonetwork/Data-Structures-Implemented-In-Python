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


    def delete_node(self,key):
        cur_node=self.head
        if cur_node and cur_node.data==key:
            self.head=cur_node.next
            cur_node=None
            return

        prev=None
        while cur_node and cur_node.data!=key:
            prev=cur_node
            cur_node=cur_node.next

        if cur_node is None:
            return

        prev.next=None
        cur_node=None

    def delete_node_pos(self,pos):
        cur_node=self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev=None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count+=1

        if cur_node is None:
            return
        
        prev.next=cur_node.next
        cur_node=None

    def len_Iterative(self):
        count=0
        cur_node = self.head

        while cur_node:
            count+=1
            cur_node=cur_node.next
        print(count)

    def len_recursive(self,node):
        if node is None:
            return 0
        return 1+self.len_recursive(node.next)

    def swap_nodes(self,key1,key2):
        if key1 == key2:
            return
        
        prev_1 = None
        cur_node1 = self.head

        while cur_node1 and cur_node1.data != key1:
            prev_1 = cur_node1
            cur_node1 = cur_node1.next

        prev_2 = None
        cur_node2 = self.head
        while cur_node2 and cur_node2.data != key2:
            prev_2 = cur_node2
            cur_node2 = cur_node2.next

        if not cur_node1 or not cur_node2:
            return

        if prev_1:
            prev_1.next = cur_node2
        else:
            self.head = cur_node2

        if prev_2:
            prev_2.next = cur_node1
        else:
            self.head = cur_node1

        cur_node1.next,cur_node2.next = cur_node2.next,cur_node1.next

    # A->B->C->D->E->F->0
    # F->E->D->C->B->A->0
    #         OR
    # A<-B<-C<-D<-E<-F<-0

    def revITR(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def revREC(self):
        def _revREC(cur,prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _revREC(cur,prev)
        self.head =  _revREC(cur = self.head , prev = None)

    def merge_sorted(self,llist):
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data<=q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head  = s

        while p and q:
            if p.data<=q.data:
                s.next = p
                s = p
                p = s.next
        
            if q.data<=p.data:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q

        if not q:
            s.next = p

    
    def Remove_Duplicates(self):
        prev = None
        cur = self.head
        dupli = dict()

        while cur:
            if cur.data in dupli:
                prev.next = cur.next
                cur = None

            else:
                dupli[cur.data] = 1
                prev = cur
            cur = prev.next



llist1 = LinkedList()
llist2 = LinkedList()

llist1.append(1)
llist1.append(5)
llist1.append(7)
llist1.append(9)
llist1.append(10)

llist2.append(2)
llist2.append(3)
llist2.append(4)
llist2.append(6)
llist2.append(8)


llist1.print_list()
print("\n")
llist2.print_list()
print("\n")
llist1.merge_sorted(llist2)
llist1.print_list()


