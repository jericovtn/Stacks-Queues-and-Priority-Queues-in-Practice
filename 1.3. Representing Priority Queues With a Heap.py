# Name: Jerico James F. Viteño
# Laboratory Exercise 4: Stacks, Queues, and Priority Queues in Practice
# 1. Implementing Queues in Python
# November 19, 2022

# 3. Representing Priority Queues With a Heap
# First function in building a Priority Queue 
from heapq import heappush

fruits = []

heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)

# Second function in building a Priority Queue 
from heapq import heappop

print(heappop(fruits))
print(fruits)