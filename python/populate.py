from generator import age_gen
from generator import ph_gen
from generator import name_gen
from generator import dob_gen

#print('Name : ' + name_gen())
#print('Age : ' + str(age_gen()))
#print('Phone : ' + ph_gen())

PIPE = '|'
LINE = '\n'
for i in range(1,20):
    with open('person.txt','a') as out:
        dob = dob_gen()
        out.write(name_gen() + PIPE + str(age_gen(dob)) + PIPE + dob + PIPE + ph_gen() + LINE )
