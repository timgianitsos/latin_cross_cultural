#pylint: disable = invalid-name, missing-docstring
import csv

reader = csv.reader(open('stylometry_data_expected.csv', mode='r'))
next(reader)
expected_names = {row[28] for row in reader}

reader = csv.reader(open('stylometry_data_result.csv', mode='r'))
next(reader)
result_names = {row[28] for row in reader}

print(sorted(list(expected_names - result_names)))
print()
# print(result_names - expected_names)
