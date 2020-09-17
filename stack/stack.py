"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
'''
# using an array
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.append(value)

    def pop(self):
        if len(self.storage) != 0:
            self.size -= 1
            last = self.storage[-1]
            self.storage.remove(last)
            return last
        else:
            return None
'''
# using a linked list
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

class Stack:
    def __init__(self):
        self.size = 0
        self.top = None
       
    def __len__(self):
        return self.size

    def push(self, value):
        new_node = Node(value)
        self.size += 1
        if self.top == None:
            self.top = new_node
        else:
            old_top = self.top
            self.top = new_node
            self.top.set_next(old_top)

    def pop(self):
        if self.top != None:
            self.size -= 1
            old_top = self.top
            self.top = old_top.get_next()
            return old_top.value
        else:
            return None

