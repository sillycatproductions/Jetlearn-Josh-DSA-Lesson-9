# Inorder : Left - Data (Middle) - Right
# Postorder : Left - Right - Data
# Preorder : Data - Left - Right

# main code start -------------------------------------------------------------------------:

class Node(): # defines left, right and data (data is a (root))
    def __init__(self, a):
        self.left = None
        self.right = None
        self.data = a

def inorder(root): # inorder pattern
    if root: # only if first node exists
        inorder(root.left) # defines the pattern
        print(root.data) # line 15
        inorder(root.right) # line 15

def postorder(root): # postorder pattern
    if root: # line 14
        postorder(root.left) # line 15
        postorder(root.right) # line 15
        print(root.data) # line 15

def preorder(root): # preorder pattern
    if root: # line 14
        print(root.data) # line 15
        preorder(root.left) # line 15
        preorder(root.right) # line 15

# main code end -------------------------------------------------------------------------:

# object start --------------------------------------------------------------------------:

root = Node(500) # top (parent of tree)

root.left = Node(120) # left (child of root)

root.right = Node(238) # right (child of root)

root.left.left = Node(40) # left child of left
root.left.right = Node(60) # right child of left

root.right.left = Node(2) # left child of right
root.right.right = Node(27) # right child of right

root.left.left.left = Node(4) # left child of left child of left
root.left.left.right = Node(6) # right child of left child of left
root.left.right.left = Node(7) # left child of right child of left
root.left.right.right = Node(8) # right child of right child of left

root.right.left.left = Node(3) # left child of left child of right
root.right.left.right = Node(11) # right child of left child of right
root.right.right.left = Node(1) # left child of right child of right
root.right.right.right = Node(5) # right child of right child of right

# object end -------------------------------------------------------------------------:

# print start ------------------------------------------------------------------------:

print('Inorder Traversal: ') 
inorder(root)

print('Postorder Traversal: ')
postorder(root)

print('Preorder Traversal: ')
preorder(root)

# print end --------------------------------------------------------------------------: