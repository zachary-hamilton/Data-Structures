"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        list_node = ListNode(value)
        if self.tail == None and self.head == None: # if linked list is empty
            self.length += 1
            self.head = list_node
            self.tail = list_node
        else:
            self.length += 1
            self.head.prev = list_node
            old_head = self.head
            self.head = list_node
            self.head.next = old_head
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 1: # if there is one entry and head and tail are the same
            self.length -= 1
            old_head = self.head
            self.tail = None
            self.head = None
            return old_head.value
        elif self.length > 1: # if there are multiple items in the linked list
            self.length -= 1
            old_head = self.head
            self.head = self.head.next
            self.head.prev = None
            return old_head.value
        else:  # if the linked list is empty
            return None

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        list_node = ListNode(value)
        if self.tail == None and self.head == None: # if linked list is empty
            self.length += 1
            self.head = list_node
            self.tail = list_node
        else:
            self.length += 1
            self.tail.next = list_node
            old_tail = self.tail
            self.tail = list_node
            self.tail.prev = old_tail
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 1: # if there is one entry and head and tail are the same
            self.length -= 1
            old_tail = self.tail
            self.tail = None
            self.head = None
            return old_tail.value
        elif self.length > 1: # if there are multiple items in the linked list
            self.length -= 1
            old_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return old_tail.value
        else: # if the linked list is empty
            return None
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node.next == None and node.prev == None: # if only one element in list
            pass
        elif node.prev == None: # head is already at the front           
            pass
        elif node.next == None: # this will move the tail 
            old_head = self.head
            old_head.prev = node

            self.tail = self.tail.prev
            self.tail.next = None

            self.head = node
            self.head.prev = None
            self.head.next = old_head
        else: # this will move an item in the middle
            before_node = node.prev
            after_node = node.next
            before_node.next = after_node
            after_node.prev = before_node

            old_head = self.head
            old_head.prev = node

            self.head = node
            self.head.prev = None
            self.head.next = old_head    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node.next == None and node.prev == None: # if only one element in list
            pass
        elif node.prev == None: # this will move the head            
            old_tail = self.tail
            old_tail.next = node

            self.head = self.head.next
            self.head.prev = None

            self.tail = node
            self.tail.next = None
            self.tail.prev = old_tail
        elif node.next == None: # tail is already at the end
            pass
        else: # this will move an item in the middle
            before_node = node.prev
            after_node = node.next
            before_node.next = after_node
            after_node.prev = before_node

            old_tail = self.tail
            old_tail.next = node

            self.tail = node
            self.tail.next = None
            self.tail.prev = old_tail
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node.next == None and node.prev == None: # if only one element in list
            self.length = 0
            self.head = None
            self.tail = None
        elif node.prev == None: # this will delete the head
            self.length -= 1
            self.head = self.head.next
            self.head.prev = None
        elif node.next == None: # this will delete the tail
            self.length -= 1
            self.tail = self.tail.prev
            self.tail.next = None
        else: # this will delete an item in the middle
            self.length -= 1
            before_node = node.prev
            after_node = node.next
            before_node.next = after_node
            after_node.prev = before_node
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current_node = self.head
        value_list = []
        for i in range(self.length):
            value_list.append(current_node.value)
            current_node = current_node.next
        return max(value_list)



