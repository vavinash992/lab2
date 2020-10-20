# Defining the Node class
class Node:
    def __init__(self,data): # Constructor for Node class
        self.data = data
        self.prev = None
        self.next = None

# Definind the Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Method to append new nodes
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    # Method to Print Nodes of Linked List
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end = ' ')
            cur = cur.next
    

dll = DoublyLinkedList()
n = int(input("Enter the size of the linked list : "))
print("Enter the elements of the linked list")
for i in range(n):
    dll.append(input())

dll.print_list()
