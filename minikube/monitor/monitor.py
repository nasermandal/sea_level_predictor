import time
import requests
from datetime import datetime

url = "http://model-service:5000"

while True:
    try:
        start_time = time.time()
        response = requests.get(url)
        latency = time.time() - start_time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ✅ Status: {response.status_code}, Latency: {latency:.3f}s")
    except Exception as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ❌ Request failed: {e}")
    time.sleep(10)  # Adjust interval as needed

