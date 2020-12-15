class Node:
    def __init__(self,data): # Constructor for Node class
        self.data = data
        self.next = None

# Defining the Linked List class
class LinkedList:
    def __init__(self): # Constrctor for LinkedList class
        self.head = None

    # Method to append data
    def append(self,data):
        new_node = Node(data)
        # If head is empty
        if self.head is None:
            self.head = new_node
            return
        # If head is not empty
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
    
    # Method to print linked list
    def print_list(self):
        if self.head is None:
            print("EMPTY LINKED LIST")
            return
        cur = self.head
        while cur:
            # Traversing through each element and printing it
            print(cur.data)
            cur = cur.next
     
    # Method for maximum and minimum elements in linked list
    def min_max(self):
        if self.head is None:
            print("EMPTY LINKED LIST")
            return (None,None)
        cur = self.head
        mini = None
        maxi = None
        while cur:
            # Traversing through each element
            d = cur.data
            if mini==None or d<mini:
                mini = d
            if maxi==None or d>maxi:
                maxi = d
            cur = cur.next
        return (mini,maxi)
        

ll = LinkedList() # Creating a linked list
size = int(input("Enter the number of elements you want to add to the Linked List : "))
# Appending data to it
for i in range(size):
    k = int(input("Enter the data : "))
    ll.append(k)
# Printing the linked list
print("The Linked List: ")
ll.print_list()

# Printing the aximum and minimum of the linked list
mi,ma = ll.min_max()
print("The minimum element is",mi)
print("The maximum element is",ma)
