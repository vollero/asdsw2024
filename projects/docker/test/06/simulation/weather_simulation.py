import time
import random
from influxdb import InfluxDBClient

INFLUXDB_ADDRESS = 'influxdb'
INFLUXDB_USER = 'admin'
INFLUXDB_PASSWORD = 'admin'
INFLUXDB_DATABASE = 'weather'

def main():
    client = InfluxDBClient(host=INFLUXDB_ADDRESS, port=8086, username=INFLUXDB_USER, password=INFLUXDB_PASSWORD, database=INFLUXDB_DATABASE)

    while True:
        temperature = 20 + 10 * random.random()
        humidity = 50 + 20 * random.random()

        json_body = [
            {
                "measurement": "weather",
                "tags": {
                    "location": "office"
                },
                "fields": {
                    "temperature": temperature,
                    "humidity": humidity
                }
            }
        ]

        client.write_points(json_body)
        print(f"Written data: {json_body}")
        time.sleep(5)

if __name__ == '__main__':
    main()

