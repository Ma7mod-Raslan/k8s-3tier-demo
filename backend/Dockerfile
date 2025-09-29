FROM python:3.11-alpine

WORKDIR /app

COPY requirments.txt /app

RUN pip install -r requirments.txt --no-cache-dir

COPY app.py /app

CMD ["python", "app.py"]