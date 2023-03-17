import csv
from datetime import datetime
import random

fieldnames = ['horodatage', 'temperature', 'humidite']

datas = []

with open('datas.csv', 'r') as csvfile:
    try:
        spamreader = csv.DictReader(csvfile)

        for row in spamreader:
            horodatage = datetime.strptime(
                row['horodatage'], '%Y-%m-%d %H:%M:%S')

            datas.append({
                'horodatage': horodatage,
                'temperature': row['temperature'],
                'humidite': row['humidite']
            })

    except IOError:
        exit()


def add_data(temperature: float, humidite: float):
    horodatage = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    while len(datas) > 30:
        datas.pop(0)

    datas.append({
        'horodatage': horodatage,
        'temperature': temperature,
        'humidite': humidite
    })

    try:
        with open('datas.csv', 'w+', newline='') as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames)

            csvwriter.writeheader()
            csvwriter.writerows(datas)

    except IOError:
        exit()


# Generate random datas in CSV file
for _ in range(50):
    add_data(random.randrange(20, 40), random.randrange(20, 70))
