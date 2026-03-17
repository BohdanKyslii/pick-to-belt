FROM python:3.11-slim

WORKDIR /app

# System deps для smbus2 на Pi
RUN apt-get update && apt-get install -y --no-install-recommends \
    i2c-tools \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/data /app/static/uploads

EXPOSE 5000

CMD ["python", "run.py"]
