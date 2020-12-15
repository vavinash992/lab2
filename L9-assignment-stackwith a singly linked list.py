class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def remove_head(self):
        if self.head and self.head.next:
            d = self.head
            self.head = self.head.next
            d.next = None
        return d.data

    def printlist(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()


class StackLL:
    def __init__(self):
        self.items = LinkedList()

    def push(self, data):
        self.items.add_at_end(data)

    def pop(self):
        return self.items.remove_head()

    def peek(self):
        return self.items.tail.data

    def printstack(self):
        self.items.printlist()

s = StackLL()
print("Select a choice :")
print("1. PUSH")
print("2. POP")
print("3. DISPLAY")
print("4. EXIT")
while True:
    choice = int(input("Enter a choice number (1/2/3/4) : "))
    if choice==1:
        data = input("Enter the element you wanna push in the stack : ")
        s.push(data)
    elif choice==2: print("The popped element is", s.pop())
    elif choice==3:
        print("The stack is : ")
        s.printstack()
    elif choice==4:
        print("----The menu is closed----")
        break
    else: print("Enter a valid choice")
