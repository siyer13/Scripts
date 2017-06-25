problem = '''
Write a funtion to generate a random 4digit unique even number,
the four digits cannot be the same, 1234
is valid, but 1134 is not valid
'''

import random
num_set = set()
flag = True

while flag:
    for i in range(0,4):
        r = random.randint(0,9)
        num_set.add(r)
        #print num_set
    # check if the set has less than 4 elements or if the first element in the list is 0
    # first element 0 makes only a 3digit number
    # check the last even number
    if len(num_set) < 4 or list(num_set)[0] == 0 or list(num_set)[3] % 2 != 0:
        #print num_set
        num_set = set()
    else:
        flag = False

#print num_set
print list(num_set)[0]

random_number = list(num_set)[0] * 1000 + list(num_set)[1] * 100 + list(num_set)[2] * 10 + list(num_set)[3] * 1
print random_number
