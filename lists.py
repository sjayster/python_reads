"""
Linked List:

For a singly linked list, we start off by having 2 classes - 1 for the Node and the other for the List.

Node class:

The node class has the bones for creating a node in a list. It contains the data and the address/next part.
Imagine this to be a box that has 2 partitions, one for the data and the other for the address of the next node.

Functions:
The essential functions in the Node class are all related to the 2 fields present in it.
Data -> getData(): returns the data of a given node and setData(newdata): set the data of a node to a given value
next -> getNext(): returns the address of the next node and setNext(newnext): set the next field to a given address

The above class and functions give us the building blocks to a linked list node

List class:

To start with, the list class creates a head object that points to None.
The list class contains the elements of the list and operations to play around with the list.
List makes use of the functions defined in the Node class to manipulate the objects.

Essential functions:

1. isEmpty() - If the list is empty (head == None), returns True
2. add(data) - The simplest way to add an element is to add it to the front of the list.
   Steps:
	a. Create a temp Node along with the value
	b. Set the next part of the temp node to the next of the head
	c. Finally, make the temp node as the head.

	example add(5) to a list that has 1-> 2-> 8-> None
	Here, 1 is the head node. 
	Step a: temp node has data set to 5 => temp = 5
	Step b: set temp's next to head => 5-> 1-> 2-> 8-> None temp = 5 and head = 1
	Step c: Make temp as the head => 5-> 1-> 2-> 8-> None temp = 5 and head = 5

3. size() - Return the number of elements in the list.
   Steps:
    a. Have the head pointing to a temp node, call it current. current = head, current points to 5
    b. Have a variable to track the number of elements in the list
    c. While the current node is not empty, increment the count by 1
    d. Once the list ends, meaning current == None, return the count

4. search(search_item) - Return True if an element is present.
   Steps:
    a. It follows the same set of steps as size, except, we issue getData() on the current node to see if the value is same as the search_item.
       If it is found, we return True.
    b. If we reach the end of the list, we return False

5. delete(item):
   This is the tricky part in linked list. We need to consider 2 scenarios. The element that needs to be deleted can be present at the head of the list or anywhere else.
   We need to know what was the previous node, in order to move the reference.

   Let us consider this list - (head)17-> 26-> 93-> 17-> 77-> 17-> None
   We need to delete all the 17's present in the list.

   Steps:
    a. Have 2 objects - current and previous. current points to the head and previous points to None to start with.
    b. While current is not None, check if current's data == item to be deleted.
    c. If a match is found:
       1. Check to see if previous is None. If so, that means the head node needs to be deleted.
          We set current to current's next and make current the head
       2. If it is not the head node, we set previous-> next to current's-> next and set current to current's next
    d. If a match is not found:
       Set previous to the current node and current to current's-> next

    Example: (head)17-> 26-> 93-> 17-> 77-> 17-> None
    Item_to_be_deleted    previous    current     Match?    condition c1?     condition c2?    condition d?   new_list
         17					None		17			yes			yes 				no 				no        (head)26-> 93-> 17-> 77-> 17-> None
         								Previous remains None, current becomes 26 and head becomes 26

         17					None		26			no			no					no 				yes       (head)26-> 93-> 17-> 77-> 17-> None
         								Previous becomes 26, current becomes 93 and head remains as 26

         17					26  		93			no			no					no 			    yes       (head)26-> 93-> 17-> 77-> 17-> None
         								Previous becomes 26, current becomes 93 and head remains as 26

         17					93			17			yes			no					yes 			no        (head)26-> 93-> 77-> 17-> None
         								Previous becomes 93, current becomes 77 and head remains as 26

         17					93		    77			no			no					no 				yes       (head)26-> 93-> 77-> 17-> None
         								Previous becomes 93, current becomes 17 and head remains as 26

         17					77   		17			yes			no					yes 			no        (head)26-> 93-> 77-> None
         								Previous becomes 26, current becomes None and head remains as 26

6. Print_list()
	a. Set current as head, have an empty list to store the elements.
	b. While current is not None, append current's getData() to the list
	c. Set current to current's getNext()

"""


class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext



class List(object):
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, data):
		temp = Node(data)
		temp.setNext(self.head)
		self.head = temp

		return self.head.getData()

	def size(self):
		current = self.head
		count = 0

		while current:
			count += 1
			current = current.getNext()

		return count

	def search(self, item):
		current = self.head
		found = False

		while not found and current:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found


	def delete(self, data):
		current = self.head
		previous = None
		found = False

		while current:
			if current.getData() == data:
				found = True
				if previous == None:
					self.head = current.getNext()
					current = self.head
					
				else:
					previous.setNext(current.getNext())
					current = current.getNext()
			else:
				previous = current
				current = current.getNext()

		return found

	def print_list(self):
		current = self.head
		result = []
		while current:
			result.append(current.getData())
			current = current.getNext()

		return result

mylist = List()
print "Is the list empty? ", mylist.isEmpty()
print mylist.add(17), " was added"
print mylist.add(31), " was added"
print mylist.add(77), " was added"
print mylist.add(17), " was added"
print mylist.add(93), " was added"
print mylist.add(26), " was added"
print mylist.add(17), " was added"
print "The list has ", mylist.size(), " elements"
print "The elements are ", mylist.print_list()
print "Is 17 present? ", mylist.search(17)
print "Is 18 present? ", mylist.search(18)
print "Has all instances of 17 been deleted? ", mylist.delete(17)
print "The elements are ", mylist.print_list()
print "Has 54 been deleted? ",mylist.delete(54)
print "The list now has ", mylist.size(), " elements"
print "The elements are ", mylist.print_list()
print "Is the list empty? ", mylist.isEmpty()

"""
Sample Output:

Is the list empty?  True
17  was added
31  was added
77  was added
17  was added
93  was added
26  was added
17  was added
The list has  7  elements
The elements are  [17, 26, 93, 17, 77, 31, 17]
Is 17 present?  True
Is 18 present?  False
Has all instances of 17 been deleted?  True
The elements are  [26, 93, 77, 31]
Has 54 been deleted?  False
The list now has  4  elements
The elements are  [26, 93, 77, 31]
Is the list empty?  False

"""






