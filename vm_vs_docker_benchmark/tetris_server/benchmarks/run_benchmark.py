import psutil
import time
import json
import os
from datetime import datetime
import subprocess

RESULTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)

def measure_benchmark(duration=10):
    print("🔍 Measuring system usage while Tetris server runs...")

    cpu_usage = []
    mem_usage = []

    start_time = time.time()

    # Launch Node.js server
    server = subprocess.Popen(["node", "../tetris_server/server.js"], stdout=subprocess.DEVNULL)
    time.sleep(2)  # Give time to initialize

    try:
        while time.time() - start_time < duration:
            cpu = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory().percent
            cpu_usage.append(cpu)
            mem_usage.append(mem)
    finally:
        server.terminate()

    return {
        "cpu_avg": sum(cpu_usage) / len(cpu_usage),
        "mem_avg": sum(mem_usage) / len(mem_usage),
        "cpu_raw": cpu_usage,
        "mem_raw": mem_usage
    }

if __name__ == "__main__":
    result = measure_benchmark()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(os.path.join(RESULTS_DIR, f"benchmark_{timestamp}.json"), "w") as f:
        json.dump(result, f, indent=4)

    print("✅ Benchmark complete. Results saved.")
