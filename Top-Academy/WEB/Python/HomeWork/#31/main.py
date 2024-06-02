import requests as r
import csv
import json

response = r.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)

with open("json.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=todos[0].keys(), lineterminator="\r", delimiter=";")
    writer.writeheader()
    for todo in todos:
        writer.writerow(todo)
