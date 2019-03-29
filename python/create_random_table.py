import random
import string
# generate column names

column_set = set()
for i in range(200):
    if i == 200:
        col_val = ''.join([random.choice(string.ascii_lowercase) for x in range(6)])
        column_set.add(col_val)
    else:
        col_val = ''.join([random.choice(string.ascii_lowercase) for x in range(6)])
        column_set.add(col_val)
#print(column_set)
print(len(column_set))
column_list = [col + ' varchar(10)' for col in column_set]
sql_string = ','.join(column_list)
#print(column_list)
#print(sql_string)

sql_string = 'CREATE TABLE random_table('+sql_string+')'
print(sql_string)
