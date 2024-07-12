import csv
import json
from pprint import pprint

example = [
    ["Tom", "Smith", 80, True],
    ["Alice", "Johnson", 92, False],
    ["Bob", "Williams", 75, True],
    ["Emma", "Brown", 88, False],
    ["David", "Jones", 107, True]
]


def write_csv():
    filename = 'people.csv'
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['First name', 'Last name', 'Weight', 'Is male'])
        writer.writerows(example)

def write_json():
    filename = 'people.json'
    data = [
        {'First name': first_name, 'Last name': last_name, 'Weight': weight, 'Is male': is_male}
         for first_name, last_name, weight, is_male in example
    ]
    pprint(data)

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    #write_csv()
    write_json()