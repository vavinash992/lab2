class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)

    def insert(self,val):
    	node = Node(val)
    	q = [self.root]
    	while len(q)!=0:
    		n = q.pop(0)
    		if n.left == None:
    			n.left = node
    			break
    		else: q.append(n.left)
    		if n.right == None:
    			n.right = node
    			break
    		else: q.append(n.right)

    def preorder(self,start,traversal):
        if start:
            traversal += str(start.value)+"-"
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal 
    
    def inorder(self,start,traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += str(start.value)+"-"
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self,start,traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += str(start.value)+"-"
        return traversal


tree = BinaryTree(100)
for i in range(11):
	tree.insert(i)
print("Preorder traversal : ", tree.preorder(tree.root,''))
print("Inorder traversal : ", tree.inorder(tree.root,''))
print("Postorder traversal : ", tree.postorder(tree.root,''))
