FROM python:3.9-slim

WORKDIR /app

COPY load_generator.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/app/load_generator.py"]



