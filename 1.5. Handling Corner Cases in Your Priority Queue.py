from queues import PriorityQueue

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(CRITICAL, "wipers")
messages.enqueue_with_priority(IMPORTANT, "hazard_lights")

print(messages.dequeue())
print(messages.dequeue())

# This file still exist for formality purposes only
# Codes in this file was merged in file 1.4