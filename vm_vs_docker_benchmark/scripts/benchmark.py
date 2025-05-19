import psutil
import time
import csv
import os
import platform
from datetime import datetime

# Crear carpeta de resultados si no existe
results_dir = os.path.join(os.path.dirname(__file__), "..", "results")
os.makedirs(results_dir, exist_ok=True)

# Determinar sistema operativo
is_windows = platform.system() == "Windows"

# Preguntar entorno
env = ""
while env.lower() not in ["vm", "docker"]:
    env = input("¿Estás ejecutando esto en 'vm' o 'docker'? ").strip().lower()

# Configuración
duration = 60  # segundos
interval = 1
data = []

print(f"📊 Iniciando benchmark por {duration} segundos en entorno {env.upper()}...")

start_time = time.time()

while time.time() - start_time < duration:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu_percent = psutil.cpu_percent(interval=None)
    memory = psutil.virtual_memory()
    num_procs = len(psutil.pids())

    if not is_windows:
        load1, load5, load15 = os.getloadavg()
    else:
        load1 = load5 = load15 = 0.0

    data.append({
        "timestamp": timestamp,
        "cpu_percent": cpu_percent,
        "memory_percent": memory.percent,
        "memory_used_mb": memory.used / (1024 * 1024),
        "load_avg_1": load1,
        "load_avg_5": load5,
        "load_avg_15": load15,
        "num_processes": num_procs,
        "environment": env
    })

    time.sleep(interval)

print("✅ Benchmark finalizado.")

# Guardar CSV en modo append
csv_path = os.path.join(results_dir, f"benchmark_{env}.csv")
file_exists = os.path.isfile(csv_path)

with open(csv_path, "a", newline="") as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if not file_exists:
        writer.writeheader()
    writer.writerows(data)

# Guardar resumen TXT aparte
now = datetime.now().strftime("%Y%m%d_%H%M%S")
txt_path = os.path.join(results_dir, f"benchmark_{env}_{now}.txt")
with open(txt_path, "w") as f:
    f.write(f"Benchmark ejecutado en entorno: {env.upper()}\n")
    f.write(f"Duración: {duration} segundos\n")
    f.write(f"Número de muestras: {len(data)}\n\n")
    f.write("Resumen final:\n")
    f.write(f"CPU promedio: {sum(d['cpu_percent'] for d in data)/len(data):.2f}%\n")
    f.write(f"Memoria promedio: {sum(d['memory_percent'] for d in data)/len(data):.2f}%\n")
    f.write(f"Procesos promedio: {sum(d['num_processes'] for d in data)/len(data):.2f}\n")

print(f"📁 Resultados agregados a: {csv_path}")
print(f"📝 Resumen guardado en: {txt_path}")
