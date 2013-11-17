import os.path
import csv

competer_list_file = os.path.join(os.path.dirname(__file__), 'competers.csv')

def add_competer_to_file(company):
    with open(competer_list_file, "a") as f:
            f.write(company)
            f.write(',')

def get_competer_list():
    reader = csv.reader(open(competer_list_file, "rb"), delimiter = ",", skipinitialspace=True)
    result = []
    for r in reader:
        result.append(r)
    return result[0]
