import requests
import time
from datetime import datetime

URL = "http://model-service:5000"

while True:
    try:
        start = time.time()
        response = requests.get(URL)
        latency = time.time() - start
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}]  Status: {response.status_code} | Latency: {latency:.3f} seconds")
    except requests.exceptions.RequestException as e:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}]  Error: {e}")
    time.sleep(10)  # will test every 10s 

