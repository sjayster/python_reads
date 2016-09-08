#!/usr/bin/python

"""
Stack is a LIFO data structure. Meaning, the element that was added towards the end will be removed first.
The elements are added in a sequential fashion.
If elt1 is added to stack[0], elt2 will be added to stack[1]
Higher the index, newer the element. And the newest element will be popped first.

Essential stack operations are:
1. Check to see if the stack is empty - isEmpty()
2. Add an element to the stack - push()
3. Return the top most element of the stack - top()
4. Remove an element from the stack - pop()
5. Get the size of the stack - size()
6. Print the contents of the stack - print_stack()

"""

class Stack(object):
	def __init__(self):
		# Initialize an empty array
		self.mystack = []

	def isEmpty(self):
		# Check to see if the stack is an empty list, if yes, return True for isEmpty()
		return self.mystack == []

	def top(self):
        # Return the top most element (element that was recently added to the stack)
		return self.mystack[-1]

	def push(self, val):
		# Add an element to the stack
		self.val = val
		self.mystack.append(self.val)
		print self.val, " was added"
		return self.mystack # not needed, but just for reference

	def pop(self):
		# Remove the last element from the stack
		return self.mystack.pop()

	def size(self):
		# Size of the stack
		return len(self.mystack)

	def print_stack(self):
		# Print out the contents of the stack
		return self.mystack

# Initialize a stack object
s = Stack()
print "Is the stack empty?", s.isEmpty()
print s.push(2)
print s.push(20)
print s.push(200)
print s.push(2000)
print "Popped elt is ", s.pop()
print s.print_stack()
print s.push(1)
print s.push(10)
print "Top of the stack is ", s.top()
print "Is the stack empty?", s.isEmpty()
print "Stack has %d elements" %(s.size())
print "Popped element is ", s.pop()
print s.print_stack()


"""
Sample output:

Is the stack empty? True
2  was added
[2]
20  was added
[2, 20]
200  was added
[2, 20, 200]
2000  was added
[2, 20, 200, 2000]
Popped elt is  2000
[2, 20, 200]
1  was added
[2, 20, 200, 1]
10  was added
[2, 20, 200, 1, 10]
Top of the stack is  10
Is the stack empty? False
Stack has 5 elements
Popped element is  10
[2, 20, 200, 1]
"""
