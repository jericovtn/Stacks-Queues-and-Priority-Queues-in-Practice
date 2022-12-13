from queues import PriorityQueue

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()

# For 4. Building a Priority Queue Data Type
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# For 5. Handling Corner Cases in Your Priority Queue
messages.enqueue_with_priority(CRITICAL, "wipers")
messages.enqueue_with_priority(IMPORTANT, "hazard_lights")

# Print for 4
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())

# Print for 5
print(messages.dequeue())
print(messages.dequeue())