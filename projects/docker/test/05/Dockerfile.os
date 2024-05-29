FROM python:3.8-slim

WORKDIR /app

COPY object_storage.py /app

RUN pip install flask

EXPOSE 5000

CMD ["python", "object_storage.py"]
