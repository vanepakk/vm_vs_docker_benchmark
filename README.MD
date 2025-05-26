# VM vs Docker Benchmark

Este proyecto compara el rendimiento de una aplicación ejecutándose en una Máquina Virtual (VM) vs Docker. Utiliza un servidor Flask y realiza benchmarks de CPU, RAM y latencia durante 60 segundos. Los resultados se guardan en archivos CSV y TXT, y se visualizan con un Jupyter Notebook.

## Configuración del entorno de prueba
Host: máquina física con sistema Linux o WSL2, 8 GB RAM, 4 núcleos.

VM: Ubuntu 22.04 con 2 vCPU, 4 GB RAM.

Docker: imagen base de Python 3.9 + dependencias instaladas desde requirements.txt.

Entorno común: scripts idénticos, misma duración de benchmark (60s), mismo servidor Flask simulado.


##  Métricas y herramientas utilizadas

- Se midieron 3 métricas clave durante la ejecución:

    - Latencia promedio de respuesta del servidor Flask

    - Uso de CPU (%) del proceso Python

    - Uso de RAM (MB) del proceso

- Herramientas utilizadas:

    - psutil: para métricas del sistema

    - Flask: servidor HTTP simulado

    - pandas, matplotlib: para análisis y visualización

    - Jupyter Notebook: para visualizar los resultados


## 📁 Estructura del Proyecto

```bash
vm_vs_docker_benchmark/
├── notebooks/
│ └── vm_vs_docker_comparison.ipynb ← Jupyter Notebook para visualización
├── results/ ← Resultados generados automáticamente
│ ├── benchmark_vm.csv
│ ├── benchmark_docker.csv
│ └── ...
├── scripts/
│ ├── benchmark.py ← Script principal de benchmarking
│ ├── run_server.py ← Servidor Flask simulado
│ ├── docker_setup.sh ← Inicializador para Docker
│ └── vm_setup.sh ← Inicializador para VM
├── tetris/ ← Código del servidor simulado
│ ├── index.html
│ ├── game.js
│ └── style.css
├── requirements.txt ← Dependencias Python
└── README.md ← Este archivo
```

## ⚙️ Instalación de dependencias

Primero, asegúrate de tener Python 3 instalado.

1. Abre una terminal en la raíz del proyecto.
2. Ejecuta:

```bash
pip install -r requirements.txt
```

Esto instalará:

- Flask

- pandas

- Matplotlib

- Psutil

- JupyterLab

## 🚀 Cómo ejecutar el benchmark

1. Iniciar el servidor simulado

```bash
cd scripts
python run_server.p
```

Esto levantará un servidor en http://localhost:8000.

2. Ejecutar benchmark
En otra terminal, ejecuta:

```bash
cd scripts
python benchmark.py
```

Este script te preguntará si estás ejecutando desde una vm o docker. Después de 60 segundos, guardará los resultados en la carpeta results/.

## 📊 Visualizar los resultados

1. Inicia Jupyter Lab o Notebook
```bash
jupyter lab
```

O:
```bash
jupyter notebook
```

Abre el archivo:

`notebooks/vm_vs_docker_comparison.ipynb`
Este notebook generará gráficos comparativos de:

- Latencia

- Uso de CPU

- Uso de RAM

Basados en los archivos CSV generados por el benchmark.

---

AQUI FOTOS DE LOS GRAFICOS DE `/notebooks` Y archivos .txt de la carpeta `/results`.

---

## 🧼 Recomendaciones
Ejecuta los benchmarks por separado: una vez desde Docker, otra desde la VM.

Asegúrate de no tener procesos pesados corriendo durante las pruebas.

Si usas WSL, asegúrate de que Jupyter y los scripts corren en el mismo entorno.

## 🛠 Requisitos

- Python 3.8+

- pip

- Docker (si usarás el contenedor)

- JupyterLab o Jupyter Notebook

## Los resultados se encuentran en archivos .csv dentro de `results/`.

El notebook vm_vs_docker_comparison.ipynb genera gráficos como:

- Evolución temporal de la latencia

- CPU y RAM a lo largo del tiempo

(Opcional) Gráfico radar (de araña) para comparar rendimiento global.