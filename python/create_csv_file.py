import csv
import random
import string


def make_csv_list():
    csv_list = []
    for i in range(600):
        csv_list.append(''.join([random.choice(string.ascii_letters) for x in range(6)]))
    return csv_list



#print(csv_list)
with open('insert_file.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(30000):
        print(i)
        csv_writer.writerow(make_csv_list())
    print("FINISHED")
