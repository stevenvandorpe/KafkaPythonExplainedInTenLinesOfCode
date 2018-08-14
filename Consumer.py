from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     auto_commit_interval_ms=1000,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('localhost:27017')
collection = client.PcPerformance.PcPerformance

for message in consumer:
    message = message.value
    id = collection.insert_one(message).inserted_id
    print('{} added to {}'.format(message, collection))

