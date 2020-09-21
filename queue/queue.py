"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# using array
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):     
        if len(self.storage) != 0:
            self.size -= 1
            first = self.storage[0]
            self.storage.remove(first)
            return first
        else:
            return None

# using linked list

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)
        self.size += 1
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def dequeue(self):
        if self.head != None:
            self.size -= 1
            old_head = self.head
            self.head = old_head.get_next()
            return old_head.value
        else:
            return None

# An array is storing all of the values at once together while in a linked list only the head and tail 
# are saved in the queue and would have to iterate throu each node to get all of the values.

# stretch
# You would need two stacks, one for the head and one for the tail
'''
from stack import Stack


class Queue:
    def __init__(self):
        self.headstack = Stack()
        self.tailstack = Stack()
        self.size = 0
        self.head = self.headstack.top
        self.tail = self.tailstack.top
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)
        self.size += 1
        if self.head == None and self.tail == None:
            self.headstack.push(new_node)
            self.tailstack.push(new_node)
            self.head = self.headstack.top
            self.tail = self.tailstack.top
        else:
            self.tailstack.push(new_node)
            self.tail = self.tailstack.top

    def dequeue(self):
        if self.head != None:
            self.size -= 1
            old_head = self.headstack.top
            self.headstack.pop()
            if len(self.headstack) == 0:
                while len(self.tailstack) != 0:               
                    intermediate_node = self.tailstack.top
                    print(f'current top of tailstack: {intermediate_node.value.value}')
                    print(f'current top of headstack: {self.headstack.top}')
                    self.headstack.push(intermediate_node.value)
                    self.tailstack.pop()
                self.headstack.pop()
                self.head = self.headstack.top.value
                self.tail = self.tailstack.top
            else:
                self.headstack.pop()
                self.head = self.headstack.top.value
            return old_head    
        else:
            return None

woo = Queue()
woo.enqueue(8)
woo.enqueue(9)
woo.enqueue(10)
woo.enqueue(11)
print(woo.head.value.value) # expecting 8
woo.dequeue()
print(woo.head.get_next()) # expecting 9
woo.dequeue()
print(woo.head.value) # expecting 10
'''
