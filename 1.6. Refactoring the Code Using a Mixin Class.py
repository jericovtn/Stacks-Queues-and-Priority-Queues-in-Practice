from queues import PriorityQueue

Significant = 5
Important = 4
Neutral = 3
Unimportant = 2
Insignificant = 1

messages = PriorityQueue()

messages.enqueue_with_priority(Neutral, "1st Honorable Mention")
messages.enqueue_with_priority(Significant, "Valedictorian")
messages.enqueue_with_priority(Unimportant, "2nd Honorable Mention")
messages.enqueue_with_priority(Insignificant, "3rd Honorable Mention")
messages.enqueue_with_priority(Important, "Salutatorian")

print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
