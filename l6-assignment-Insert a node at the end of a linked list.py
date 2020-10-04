class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

# Function to add newnode
    def Append(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


list = LinkedList()
list.headval = Node("A")
e2 = Node("B")
e3 = Node("C")

list.headval.nextval = e2
e2.nextval = e3

list.Append("D-added node")

list.listprint()
