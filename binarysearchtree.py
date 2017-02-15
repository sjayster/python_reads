#! /usr/bin/pythom

"""
Reference:
http://www.laurentluce.com/posts/binary-search-tree-library-in-python/

Binary search Tree. The node has a data field and a left and right field.
When creating a new node, the left and right will be set to None.

Functions:

1. getRoot()
Returns the value of the current node

2. setRoot(value)
Set the value of the node to the specified value

3. getLeft()
Return current node's left element

4. getRight()
Return current node's right element

5. insert(value)

If the value is less than the value of the root, it needs to be inserted to the left
1. If current node's left is None, create a new node Node(value)
2. If not, move to current's left and call the insert function with the value

If the value is greater than the value of the root, it needs to be inserted to the right
1. If current node's right is None, create a new node Node(value)
2. If not, move to current's right and call the insert function with the value

6. lookup(value, parent=None) - returns node, parent of the node
Use the same logic as the insert function. We also have parent as an argument to get the parent of the node to be found.

1. If current's data == value, return the data and the parent
2. If data < current's data, check if current's left is None, return None, None
   If not, call lookup and set parent to current node. lookup(value, current)
3. If data < current's data, check if current's right is None, return None, None.
   If not, call lookup and set parent to current node. lookup(value, current)

7. children()
Initialize the counter to 0
If current has a left, increment by 1 and if current has a right, increment by 1 and return counter


8. delete(value)

1. We need to see if the value is present in the tree using lookup. If not, return
2. Once we get the node, call the children() to get the number of children
3. There are 3 possible cases,

a. The node to be deleted is a leaf node
   Case 1:
   if parent.left is the node to be deleted, set it to None
   if parent.right is the node to be deleted, set it to None
   del node

   Case 2:
   If the node to be deleted is the root and it has no children, set root.setRoot(None)

b. The node to be deleted has one child

   if node.left or node.right is present, set it to a temp variable called 'child'
   We need to set parent's left or right to child, depending on the node to be deleted.
   There may be a possibility that we are deleting the root node. example: Delete 5 in None <-- 5 --> 8

   Case 1:
   Deleting non root node. Meaning, parent is not None.
   If parent.left is the node, set parent.next to child else set parent.right to the child

   Case 2:
   Delete root node. If parent is None.
   Set node's value to child's value and node's left and right to child's left and right.

c. The node to be deleted has two children

   The simplest approach is to move one step right and then all left until None is hit.

   Get the node and parent info through the lookup function
   Set child as the right child of the node to be deleted.
   while child has a valid left node:
    assign child to parent
    set child to child's left

   Once child has no left, assign node's value to the current value of child. By doing this, we replace the value of the node to be deleted with the leaf value.
   Now, we have to set the right and left part of the modified node
   The child could have been parent's left or right.
   if parent.left == child, set parent.left = child.right else
   set parent.right to child.left


9. Print

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


class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getRoot(self):
        return self.data

    def setRoot(self, newdata):
        self.data = newdata

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def insert(self, element):

        if element < self.data:
            if self.getLeft() is None:
                self.left = Node(element)
            else:
                self.getLeft().insert(element)

        else:
            if self.getRight() is None:
                self.right = Node(element)
            else:
                self.getRight().insert(element)

    def lookup(self, value, parent=None):
        if value == self.getRoot():
            return self, parent

        elif value < self.getRoot():
            if self.getLeft() is None:
                return None, None
            return self.getLeft().lookup(value, self)

        else:
            if self.getRight() is None:
                return None, None
            return self.getRight().lookup(value, self)

    def children(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1

        return count

    def delete(self, value):
        node, parent = self.lookup(value)
        if node is None:
            return
        num_child = node.children()

        # If the node to be deleted is the leaf node

        if num_child == 0:
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
            del node

        elif num_child == 1:
            if node.left:
                child = node.left
            else:
                child = node.right

            if parent:
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child
                del node

            else:
                node.setRoot(child.getRoot())
                node.left = child.getLeft()
                node.right = child.getRight()

        else:
            child = node.right

            while child.left:
                parent = child
                child = child.getLeft()

            node.setRoot(child.getRoot())
            if parent.left == child:
                parent.left = child.right
            else:
                parent.right = child.left

    def preorder(self):
        if self.getLeft():
            self.getLeft().preorder()
        print self.getRoot()
        if self.getRight():
            self.getRight().preorder()

    def inorder(self):
        print self.getRoot()
        if self.left:
            self.getLeft().inorder()
        if self.right:
            self.getRight().inorder()

    def postorder(self):
        if self.left:
            self.getLeft().postorder()
        if self.right:
            self.getRight().postorder()
        print self.getRoot()


if __name__ == '__main__':
    root = Node(10)
    root.insert(5)
    root.preorder()
    print "\n Deleting 10"
    root.delete(10)
    print "\nPost delete\n"
    root.preorder()
    print "\n Deleting 5"
    root.delete(5)
    print "\nPost delete\n"
    root.preorder()
    root.insert(20)
    root.insert(2)
    root.insert(8)
    root.insert(30)
    root.insert(15)
    root.insert(1)
    root.insert(20)
    root.insert(7)
    root.preorder()
    print "Lookup 20"
    node, parent = root.lookup(20)
    if node is not None:
        print node.getRoot(), parent.getRoot()
    else:
        print "Node not found\n"
    print "Lookup 321"
    node, parent = root.lookup(321)
    if node is not None:
        print node.getRoot(), parent.getRoot()
    else:
        print "Node not found\n"
    print "\n Deleting 1"
    root.delete(1)
    print "\n post delete\n"
    root.preorder()
    print "\n Deleting 30"
    root.delete(30)
    print "\n Post delete\n"
    root.preorder()
    print "\n Deleting 5"
    root.delete(5)
    print "\n Post delete\n"
    root.preorder()

"""

Sample Output:

5
10

 Deleting 10

Post delete

5

 Deleting 5

Post delete

5
1
2
5
7
8
15
20
20
30
Lookup 20
20 5
Lookup 321
Node not found


 Deleting 1

 post delete

2
5
7
8
15
20
20
30

 Deleting 30

 Post delete

2
5
7
8
15
20
20

 Deleting 5

 Post delete

2
7
8
15
20
20
"""
