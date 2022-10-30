import json
import time
import random

from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 15

producer = KafkaProducer(
    bootstrap_servers="localhost:29092"
)

for i in range(1, ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"{i * 2}",
        "total_cost": round(random.uniform(999.99, 9999.99), 2),
        "items": {
            "iPhone 14": random.randint(1, 3),
            "AirPods Pro (2nd generation)": random.randint(1, 3),
            "Apple Watch Series 8": random.randint(1, 3)
        }
    }

    producer.send(
        ORDER_KAFKA_TOPIC, 
        json.dumps(data).encode("utf-8")
    )
    print(f"Sent order {i}")
    time.sleep(10)