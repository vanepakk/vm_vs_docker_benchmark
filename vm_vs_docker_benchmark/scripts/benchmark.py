import psutil
import time
import csv
from datetime import datetime
from pathlib import Path

# Ruta a la carpeta "results"
results_dir = Path(__file__).resolve().parent.parent / "results"
results_dir.mkdir(exist_ok=True)

output_csv = results_dir / "benchmark_results.csv"
output_txt = results_dir / "benchmark_summary.txt"

def run_benchmark(duration=10):
    print("⏱️ Ejecutando benchmark por", duration, "segundos...")
    cpu_data = []
    memory_data = []

    for _ in range(duration):
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        cpu_data.append(cpu)
        memory_data.append(mem)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Time", "CPU_Usage", "Memory_Usage"])
        for i in range(duration):
            writer.writerow([i + 1, cpu_data[i], memory_data[i]])

    with open(output_txt, "w") as txtfile:
        txtfile.write(f"Benchmark ejecutado: {timestamp}\n")
        txtfile.write(f"Duración: {duration} segundos\n")
        txtfile.write(f"Promedio CPU: {sum(cpu_data)/len(cpu_data):.2f}%\n")
        txtfile.write(f"Promedio Memoria: {sum(memory_data)/len(memory_data):.2f}%\n")

    print("✅ Benchmark completo. Resultados guardados en 'results/'.")

if __name__ == "__main__":
    run_benchmark()
