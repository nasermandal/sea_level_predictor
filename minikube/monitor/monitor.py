import requests
import time

URL = "http://model-service:5000"

while True:
    try:
        start = time.time()
        r = requests.get(URL)
        latency = round((time.time() - start) * 1000, 2)
        print(f"[OK] Latency: {latency} ms | Status: {r.status_code}")
    except Exception as e:
        print(f"[ERR] {e}")
    time.sleep(10)
