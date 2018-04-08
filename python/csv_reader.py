import csv
import sys

csv.field_size_limit(sys.maxsize)

file = open("team_contacts_cleaned.csv","w")
with open('team_contacts.csv','rU') as csvfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(file,quoting=csv.QUOTE_ALL)
    for row in reader:
        stripped = [col.replace('\n', ' ') for col in row]
        #file.write(','.join(stripped))
        #file.write('\n')
        writer.writerow(stripped)
file.close()
print 'Done'
