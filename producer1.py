# Name: Jerico James F. Viteño
# Laboratory Exercise 4: Stacks, Queues, and Priority Queues in Practice
# 6. Integrating Python With Distributed Message Queues
# 3. Apache Kafka: kafka-python3
# December 17, 2022

from kafka3 import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    message = input("Message: ")
    producer.send(
        topic="datascience",
        value=message.encode("utf-8"),
    )