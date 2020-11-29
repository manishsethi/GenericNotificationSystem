# -*- coding: utf-8 -*-
"""
KAFKA script for producer
"""
import json
from kafka import KafkaProducer

#-Testing-#
producer = KafkaProducer(bootstrap_servers=['104.42.236.61:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))


# START LOOP TO SEND MSG TO KAFKA TOPICS
for i in range(10):
    data = { "from ": "Test@gmail.com", "to" : "Test@gmail.com", "index" : "email", "sub": "Order " }

    #Working
    #producer.send('Target', json.dumps(data).encode('utf-8'))

    #-Testing-#
    producer.send('Target', data)

# Asynchronous by default
producer.close()
print("DONE.")