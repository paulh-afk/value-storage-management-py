import csv
from datetime import datetime

datas = []

with open('datas.csv', 'r') as csvfile:
    try:
        spamreader = csv.reader(csvfile)
        next(spamreader)

        for row in spamreader:
            horodatage = datetime.fromisoformat(row[0])

            datas.append({
                "horodatage": horodatage,
                "temperature": row[1],
                "humidite": row[2]
            })

    except IOError:
        exit()

print(datas)
