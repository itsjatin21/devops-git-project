FROM python:3.9-slim
WORKDIR /app
COPY backup.py .
CMD ["python", "backup.py"]
