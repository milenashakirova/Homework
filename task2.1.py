# 1.1

import csv
import json


filename = input("Введите название файла(csv): ")
with open(filename, 'r', encoding='utf-8') as infile, \
        open('output.json', 'w', encoding='utf-8') as outfile:
    data = []
    csvReader = csv.DictReader(infile, delimiter=',')
    for row in csvReader:
        row = {key: (None if value == "" else value) for key, value in row.items()}
        data.append(row)
    json.dump(data, outfile, indent=2)