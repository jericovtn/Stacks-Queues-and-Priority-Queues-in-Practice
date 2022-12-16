# Name: Jerico James F. Viteño
# Laboratory Exercise 4: Stacks, Queues, and Priority Queues in Practice
# 6. Integrating Python With Distributed Message Queues
# 2. Redis: redis
# December 17, 2022

import redis

# Publisher
with redis.Redis() as client:
    while True:
        message = input("Message: ")
        client.publish("chatroom", message)
        