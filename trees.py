#! /usr/bin/python

"""
Trees:

For a binary tree, we need 3 objects per class - root, left, right
The init takes the root of the tree.
set self.left and self.right to None, initially.

Key functions:

isempty(): return self.tree == None

getroot(): Return self.root
setroot(newval): Set the value of root.
self.root = newval

getleftchild(): return self.left
getrightchild(): return self.right

Print left and right child value
getleftchild().getroot(): return self.left.root
getrightchild().getroot(): return self.right.root

Insertleft(value)
if tree's left is not none, create self.left = Tree(value)
else,
    a. set temp to Tree(value)
    b. set temp.left to tree.left
    c. set tree.left to temp

Insertright(value)
if tree's right is not none, create self.right = Tree(value)
else,
    a. set temp to Tree(value)
    b. set temp.right to tree.right
    c. set tree.right to temp


Traversal:

1. Depth First Traversal:

   a. Pre-order: Root, left, right
   b. In-order: Left, root, right
   c. Post-order: Left, right, root

The rules are the same:
If tree is not None:
    print tree.root
    recursive_call(tree.left)
    recursive_call(tree.right)

"""


class BinaryTree(object):

    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def getRoot(self):
        return self.root

    def setRoot(self, newroot):
        self.root = newroot

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def insertRight(self, value):
        if self.right == None:
            self.right = BinaryTree(value)
        else:
            temp = BinaryTree(value)
            temp.right = self.right
            self.right = temp

    def insertLeft(self, value):
        if self.left == None:
            self.left = BinaryTree(value)
        else:
            temp = BinaryTree(value)
            temp.left = self.left
            self.left = temp

### Traversal ###


def preorder(tree):
    # Root, left, right
    if tree != None:
        print tree.getRoot()
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def inorder(tree):
    # Left, root, right
    if tree != None:
        inorder(tree.getLeftChild())
        print tree.getRoot()
        inorder(tree.getRightChild())


def postorder(tree):
    # Right, left, root
    if tree != None:
        postorder(tree.getRightChild())
        postorder(tree.getLeftChild())
        print tree.getRoot()

myTree = BinaryTree("R")
myTree.insertLeft("L1")
myTree.insertRight("R2")
myTree.insertRight("R1")
print "\nPreorder traversal\n"
preorder(myTree)
print "\nInorder traversal\n"
inorder(myTree)
print "\nPostorder traversal\n"
postorder(myTree)
print "\nRoot value is \n", myTree.getRoot()
myTree.setRoot("newR")
print "\nNew Root value is \n", myTree.getRoot()
print "\nLeft child is \n", myTree.getLeftChild().getRoot()
print "\nRight child is \n", myTree.getRightChild().getRoot()


"""
Sample output:

Preorder traversal

R
L1
R1
R2

Inorder traversal

L1
R
R1
R2

Postorder traversal

R2
R1
L1
R

Root value is 
R

New Root value is 
newR

Left child is 
L1

Right child is 
R1
"""
