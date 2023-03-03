import csv
from datetime import datetime

datas = []

with open('datas.csv', 'r') as csvfile:
    try:
        spamreader = csv.reader(csvfile)

        next(spamreader, None)

        for row in spamreader:
            horodatage = datetime.fromisoformat(row[0])

            datas.append({
                "horodatage": horodatage,
                "temperature": row[1],
                "humidite": row[2]
            })

    except IOError:
        exit()


def add_data(temperature: float, humidite: float):
    horodatage = datetime.now()

    if len(datas) == 30:
        datas.pop(0)

    datas.append({
        'horodatage': horodatage,
        'temperature': temperature,
        'humidite': humidite
    })

    try:
        with open('datas.csv', 'w+') as csvfile:
            csvwriter = csv.writer(csvfile)

            csvwriter.writerow(['horodatage', 'temperature', 'humidite'])

            for i in range(len(datas)):
                list_values = list(datas[i].values())

                horodatage = list_values[0].strftime(
                    "%Y:%m:%d %H-%M-%S")
                temperature = float(list_values[1])
                humidite = float(list_values[2])

                csvwriter.writerow([horodatage, temperature, humidite])

    except IOError:
        exit()


for _ in range(50):
    add_data(30, 30)
