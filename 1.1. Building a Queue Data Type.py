# Name: Jerico James F. Viteño
# Laboratory Exercise 4: Stacks, Queues, and Priority Queues in Practice
# 1. Implementing Queues in Python
# 1. Building a Queue Data Type
# November 19, 2022

from queues import Queue

fifo = Queue("1st", "2nd", "3rd")
len(fifo)

for element in fifo:
    print(element)

len(fifo)