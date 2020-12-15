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

    # Method to find min and max Nodes of Linked List
    def min_max(self):
        cur = self.head
        mini = None
        maxi = None
        while cur:
            if mini==None or cur.data<mini:
                mini = cur.data
            if maxi==None or cur.data>maxi:
                maxi = cur.data
            cur = cur.next
        return (mini,maxi)


    

dll = DoublyLinkedList()
n = int(input("Enter the size of the linked list : "))
print("Enter the elements of the linked list")
for i in range(n):
    dll.append(int(input()))

l = dll.min_max()
print("The smallest element of the linked list : ", l[0])
print("The largest element of the linked list : ", l[1])
