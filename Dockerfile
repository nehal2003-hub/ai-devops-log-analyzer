
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY analyzer/ ./analyzer/
COPY logs/ ./logs/

CMD ["python", "analyzer/log_analyzer.py"]
