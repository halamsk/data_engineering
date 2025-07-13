import time
import json
from kafka import KafkaProducer
from openaq import OpenAQ
from dotenv import load_dotenv
import os

# Load .env file if needed
load_dotenv()

API_KEY = os.getenv("OPENAQ_API_KEY")  # Set via .env or export
assert API_KEY, "Missing OpenAQ API key"

client = OpenAQ(api_key=API_KEY)
# data = client.locations.list(parameters_id=2, limit=1000)
# print(data)

# Kafka config
# producer = KafkaProducer(
#     bootstrap_servers="localhost:9093",
#     value_serializer=lambda v: json.dumps(v).encode("utf-8")
# )
producer = None
max_retries = 30 # Give it plenty of time
retry_delay = 5 # seconds
for i in range(max_retries):
    try:
        print(f"Attempting to connect to Kafka (attempt {i+1}/{max_retries})...")
        producer = KafkaProducer(
            bootstrap_servers="localhost:9092",
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            request_timeout_ms=10000, # Increased timeout for initial metadata request
            # api_version=(0, 10, 2) # Uncomment if you face persistent API version issues
        )
        # Force a metadata refresh to confirm connection.
        # This will raise an error if the broker isn't fully ready.
        producer.bootstrap_connected()
        print("Successfully connected to Kafka!")
        break
    except (NoBrokersAvailable, KafkaTimeoutError) as e:
        print(f"Kafka connection failed: {e}. Retrying in {retry_delay} seconds...")
        time.sleep(retry_delay)
    except Exception as e:
        print(f"An unexpected error occurred during Kafka connection attempt: {e}")
        time.sleep(retry_delay)
else:
    print("Failed to connect to Kafka after multiple retries. Exiting.")
    exit(1)

producer.bootstrap_connected()
print("Successfully connected to Kafka!")

TOPIC = "air_quality"

while True:
    try:
        print("Fetching latest measurements...")
        data = client.locations.list(parameters_id=2, limit=100)
        
        for res in data.results:
            print(res.name)
            payload = {
                 "location_name": res.name
            }
            producer.send(TOPIC, value=payload)
            print("Sent:", payload)

        time.sleep(10)

    except Exception as e:
        print("Error:", e)
        time.sleep(30)
