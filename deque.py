#!/usr/bin/python

"""
Deque is a hybrid data structure that combines both stack and queue. 
An element can be added or removed from both the front and the rear of the deque.

Essential deque operations are:
1. Check to see if the deque is empty - isEmpty()
2. Add an element to the rear - addrear()   (addition will be to the leftmost side)
3. Add an element to the front - addfront() (addition will be to the rightmost side)
4. Remove an element to the rear - removeRear()
5. Remove an element to the front - removeFront()
6. Get the size of the deque - size()
7. Print the contents of the deque - print_deque()


Deque order:

					________________________________________________
add/remove from rear -> ->  new     old     older     oldest   -> -> add/remove fromfront
					_________________________________________________

"""

class deque(object):
	def __init__(self):
		# Initialize an empty array
		self.mydeque = []

	def isEmpty(self):
		# Check to see if the deque is an empty list, if yes, return True for isEmpty()
		return self.mydeque == []

	def addFront(self, val):
		# Add an element to the rightmost side of the deque
		self.val = val
		# Insert an element to the -1 index (append)
		self.mydeque.append(self.val)
		print self.val, " was added"
		return self.mydeque # not needed, but just for reference

	def addRear(self, val):
		# Add an element to the leftmost side of the deque
		self.val = val
		# Insert an element to the 0th index of the deque (insert)
		self.mydeque.insert(0, self.val)
		print self.val, " was added"
		return self.mydeque # not needed, but just for reference

	def removeRear(self):
		# Remove the element from the left most side (top of the array)
		# We use pop(0) because, by now the first element must have moved to the last position of the array

		return self.mydeque.pop(0)

	def removeFront(self):
		# Remove the element from the right most side of the deque (last element of the array [-1])
		# We use pop() to remove the last element in the array
		return self.mydeque.pop()

	def size(self):
		# Size of the deque
		return len(self.mydeque)

	def print_deque(self):
		# Print out the contents of the deque
		return self.mydeque

# Initialize a deque object
q = deque()
print "Is the deque empty?", q.isEmpty()
print q.addRear(2)
print q.addRear('character')
print q.addFront(True)
print q.addFront(2000)

print "Deque has %d elements" %(q.size())
print "Is the deque empty?", q.isEmpty()

print q.addRear("Monday Jan 1")

print "Popped elt is ", q.removeRear()
print "Dedequed element is ", q.removeFront()

print q.print_deque()

"""
Sample output:

Is the deque empty? True
2  was added
[2]
character  was added
['character', 2]
True  was added
['character', 2, True]
2000  was added
['character', 2, True, 2000]
Deque has 4 elements
Is the deque empty? False
Monday Jan 1  was added
['Monday Jan 1', 'character', 2, True, 2000]
Popped elt is  Monday Jan 1
Dedequed element is  2000
['character', 2, True]

"""