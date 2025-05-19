FROM python:3.10-slim

RUN apt update && apt install -y python3-pip git curl procps

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install jupyter matplotlib psutil

EXPOSE 8000
CMD ["python3", "scripts/run_server.py"]
