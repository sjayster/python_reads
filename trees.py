#! /usr/bin/python

"""
Trees:

For a binary tree, we need 3 objects per class - root, left, right
The init takes the root of the tree.
set self.left and self.right to None, initially.

Key functions:

isempty(): return self.tree == None

getRoot(): Return self.root
setroot(newval): Set the value of root.
self.root = newval

getleftchild(): return self.left
getrightchild(): return self.right

Print left and right child value
getleftchild().getRoot(): return self.left.root
getrightchild().getRoot(): return self.right.root

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

2. Level order traversal

We make use of two arrays (queue) to store the current node and the result.
   a. In the runningqueue, we append the root node
   b. While runningqueue is not empty, we pop the queue and add the element to the result array
   c. We add the children of the popped element (if any) to the running queue
   d. Once the loop breaks, return the result

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


def levelorder(tree):
    runningqueue = []  # appends the node and its children
    result = []  # pops the node at every level and stores the result

    # Base condition
    if not tree:
        return
    runningqueue.append(tree)
    # While the queue is not empty, pop the element and add its value to the result array
    # Append the children of the node (if exists) to the queue
    while runningqueue:
        temp = runningqueue.pop(0)
        result.append(temp.getRoot())
        if temp.getLeftChild() is not None:
            runningqueue.append(temp.getLeftChild())
        if temp.getRightChild() is not None:
            runningqueue.append(temp.getRightChild())

    return result


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    stack = []
    result = []
    current = root
    while stack or current:
        if current:
            stack.append(current)
            current = current.getLeftChild()
        else:
            current = stack.pop()
            result.append(current.getRoot())
            current = current.getRightChild()
    return result


def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    stack = []
    result = []
    current = root
    while stack or current:
        if current:
            stack.append(current)
            result.append(current.getRoot())
            current = current.getLeftChild()
        else:
            current = stack.pop()
            current = current.getRightChild()
    return result

myTree = BinaryTree("R")
myTree.insertLeft("L1")
myTree.insertRight("R2")
myTree.insertRight("R1")
myTree.insertLeft("L2")
myTree.insertLeft("L3")


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

print "Level order traversal of my tree is \n", levelorder(myTree)
print "Preorder traversal using a stack (non-recursive)"
print preorderTraversal(myTree)
"""
Sample output:


Preorder traversal

R
L3
L2
L1
R1
R2

Inorder traversal

L1
L2
L3
R
R1
R2

Postorder traversal

R2
R1
L1
L2
L3
R

Root value is 
R

New Root value is 
newR

Left child is 
L3

Right child is 
R1
Level order traversal of my tree is 
['newR', 'L3', 'R1', 'L2', 'R2', 'L1']
Preorder traversal using a stack (non-recursive)
['newR', 'L3', 'L2', 'L1', 'R1', 'R2']

"""
