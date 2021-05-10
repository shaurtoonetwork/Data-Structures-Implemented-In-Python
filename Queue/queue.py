class Queue:
    def __init__(self):
        self.elements=[]

    def enqueue(self,element):
        self.elements.append(element)

    def dequeue(self):
        self.elements.pop(0)

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.elements == []

    def frontvalue(self):
        if not self.is_empty():
            return self.elements[0]

    def get_queue(self):
        print(self.elements)





    