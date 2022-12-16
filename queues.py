# Name: Jerico James F. Viteño
# Laboratory Exercise 4: Stacks, Queues, and Priority Queues in Practice
# 1. Implementing Queues in Python
# December 17, 2022

from collections import deque

# 6
from dataclasses import dataclass

# 4. Building a Priority Queue Data Type
from heapq import heapify, heappop, heappush

# 5. Handling Corner Cases in Your Priority Queue
from itertools import count

from typing import Any

# Inserted
# 6. Refactoring the Code Using a Mixin Class
class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

# 1. Building a Queue Data Type
# Class for Queues
class Queue(IterableMixin): # Added IterableMixin for 6
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
# Does not have Class

# Class for Priority Queue
class PriorityQueue(IterableMixin): # Added IterableMixin for 6
    def __init__(self):
        self._elements = []
        # Added for 5
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        # heappush(self._elements, (-priority, value))
        # Improved Code for 5
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        # return heappop(self._elements)[1]
        #Improved Code for 5
        return heappop(self._elements)[-1]

# Data Class
@dataclass(order=True)
class Element:
    priority: float
    count: int
    value: Any

# Class for MutableMinHeap
class MutableMinHeap(IterableMixin):
    def __init__(self):
        super().__init__()
        self._elements_by_value = {}
        self._elements = []
        self._counter = count()

    def __setitem__(self, unique_value, priority):
        if unique_value in self._elements_by_value:
            self._elements_by_value[unique_value].priority = priority
            heapify(self._elements)
        else:
            element = Element(priority, next(self._counter), unique_value)
            self._elements_by_value[unique_value] = element
            heappush(self._elements, element)

    def __getitem__(self, unique_value):
        return self._elements_by_value[unique_value].priority

    def dequeue(self):
        return heappop(self._elements).value