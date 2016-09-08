#!/usr/bin/python

"""
Queue is a FIFO data structure. Meaning, the element that was added first will be removed first.
If elt1 is added to queue[0], elt2 will be added to queue[0] and elt1 will move to queue[1]
Lower the index, newer the element. And the oldest element will be dequeued first.

Essential queue operations are:
1. Check to see if the queue is empty - isEmpty()
2. Add an element to the queue - enqueue()
3. Remove an element from the queue - dequeue()
4. Get the size of the queue - size()
5. Print the contents of the queue - print_queue()

"""

class Queue(object):
	def __init__(self):
		# Initialize an empty array
		self.myqueue = []

	def isEmpty(self):
		# Check to see if the queue is an empty list, if yes, return True for isEmpty()
		return self.myqueue == []

	def enqueue(self, val):
		# Add an element to the queue
		self.val = val
		# Insert an element to the 0th index of the queue
		self.myqueue.insert(0,self.val)
		print self.val, " was added"
		return self.myqueue # not needed, but just for reference

	def dequeue(self):
		# Remove the first element from the queue
		# We use pop() because, by now the first element must have moved to the last position of the array
		return self.myqueue.pop()

	def size(self):
		# Size of the queue
		return len(self.myqueue)

	def print_queue(self):
		# Print out the contents of the queue
		return self.myqueue

# Initialize a queue object
q = Queue()
print "Is the queue empty?", q.isEmpty()
print q.enqueue(2)
print q.enqueue('character')
print q.enqueue(True)
print q.enqueue(2000)
print "Popped elt is ", q.dequeue()
print q.print_queue()
print q.enqueue(1)
print q.enqueue("Monday Jan 1")
print "Is the queue empty?", q.isEmpty()
print "Queue has %d elements" %(q.size())
print "Dequeued element is ", q.dequeue()
print q.print_queue()


"""
Sample output:

Is the queue empty? True
2  was added
[2]
character  was added
['character', 2]
True  was added
[True, 'character', 2]
2000  was added
[2000, True, 'character', 2]
Popped elt is  2
[2000, True, 'character']
1  was added
[1, 2000, True, 'character']
Monday Jan 1  was added
['Monday Jan 1', 1, 2000, True, 'character']
Is the queue empty? False
Queue has 5 elements
Dequeued element is  character
['Monday Jan 1', 1, 2000, True]

"""