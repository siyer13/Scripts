# -*- coding: utf-8 -*-
import csv
import sys


file = open("team_contacts_cleaned.csv","w")
with open('team_contacts.csv') as csvfile:
reader = csv.reader(csvfile)
for row in reader:
    stripped = [col.replace('\n', '') for col in row]
    file.write(','.join(stripped))
    file.write('\n')
file.close()
print 'Done'
