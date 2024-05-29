FROM python:3.8-slim

WORKDIR /app

COPY weather_simulation.py /app/weather_simulation.py

RUN pip install influxdb

CMD ["python", "weather_simulation.py"]
