"""
Heaps:

Functions: Insert, getMin
In a min-heap, the lowest element is at the top of the heap.
A heap typically begins at index1 as index 0 will either be the lowest number or the highest number, depending on the heap

1. Initialize heap with heap[0] = 0 and size = 0

2. Insert(value):
   a. Append the value to the heap array and increment size by 1
   b. The property of a heap is such that the elements at the top are lesser than the ones below it.
   c. Set now to current size
   d. while now/2 > 0, do the following operations,
       a. Check if heap[now] < heap[now/2], if so, swap(heap[now], heap[now/2])
       b. Set now to now/2

3. getMin():
   a. We need to return the element at 1st position -> heap[1]
   b. Save heap[1] to minval
   c. Set heap[1] to heap[size] and set size-=1. This will break the heap property. Hence, we need to rebalance it.
   d. We need to replace heap[1] with the smallest child value.
   e. Set parent = 1 and while parent*2 <= size
       a. Get the minchild position. Pass parent value to the minchild()
       b. Once we get the minchild index, if heap[child] < heap[parent], swap(heap[child], heap[parent])
       c. Set parent = child

    f. Once the loop breaks, return minval


4. minchild(parent)
   a. if parent*2 + 1 > size, return 2*i, as there is not 2*i +1 
   b. If heap[2*i] < heap[2*i + 1], return 2*i, else return 2*i + 1

"""


class Heaps(object):

    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def insert(self, value):
        self.heaplist.append(value)
        self.size += 1
        now = self.size
        while now // 2 > 0:
            if self.heaplist[now] < self.heaplist[now / 2]:
                self.heaplist[now], self.heaplist[
                    now / 2] = self.heaplist[now / 2], self.heaplist[now]
            now = now // 2

    def getMin(self):
        minval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.size -= 1
        self.heaplist.pop()
        parent = 1
        while parent * 2 <= self.size:
            child = self.minimumchild(parent)

            if self.heaplist[parent] > self.heaplist[child]:
                self.heaplist[parent], self.heaplist[child] = self.heaplist[
                    child], self.heaplist[parent]

            parent = child

        return minval

    def minimumchild(self, i):
        if (i * 2) + 1 > self.size:
            return i * 2

        if self.heaplist[(i * 2)] < self.heaplist[(i * 2) + 1]:
            return (i * 2)
        return (i * 2) + 1

    def printheap(self):
        for elt in self.heaplist:
            print elt


h = Heaps()
h.insert(10)
h.insert(21)
h.insert(84)
h.insert(9)

while h.size != 1:
    print h.getMin()
