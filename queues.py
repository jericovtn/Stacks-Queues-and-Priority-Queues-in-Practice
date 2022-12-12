# Name: Jerico James F. Viteño
# Laboratory Exercise 4: Stacks, Queues, and Priority Queues in Practice
# 1. Implementing Queues in Python
# November 19, 2022

from collections import deque
from heapq import heappop, heappush

# 1. Building a Queue Data Type
# Class for Queues
class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

# 2. Building a Stack Data Type
# Class for Stack
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

# 3. Representing Priority Queues With a Heap
# Do not have Class

# 4. Building a Priority Queue Data Type
# Class for Priority Queue

# Unfortunately, there are a few problems with this implementation
# class PriorityQueue:
#    def __init__(self):
#        self._elements = []
#   def enqueue_with_priority(self, priority, value):
#        heappush(self._elements, (priority, value))
#    def dequeue(self):
#        return heappop(self._elements)

# Fixed Code
class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (-priority, value))

    def dequeue(self):
        return heappop(self._elements)[1]
        