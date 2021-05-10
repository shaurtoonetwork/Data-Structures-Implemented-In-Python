# stack -> 1 2  3 4
class Stack:

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def top(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items())

    def get_stack(self):
        print(self.items)


s = Stack()
s.push(2)
print(get_stack())

    
