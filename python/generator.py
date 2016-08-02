import random
import os
from datetime import datetime,date

# A ten digit phone number generator
def ph_gen():
    phonenumber = ''
    for i in range(0,10):
        if i == 0:
            phonenumber = str(random.randint(0,9))
        elif i == 3 or i == 6:
            phonenumber = phonenumber + '-' + str(random.randint(0,9))
        else:
            phonenumber = phonenumber + str(random.randint(0,9))
    return phonenumber

# get a random name from list of names
def name_gen():
    data = open(r"C:\Users\Sridhar\Documents\src\python\names.txt").readlines()
    name = random.choice(data).strip()
    return name

# calculate age for a given date of birth
def age_calculator(dob):
    today = date.today()
    format_string = '%m/%d/%Y'
    date_object = datetime.strptime(dob,format_string)
    dob = date_object.date()
    age = int((date.today() - dob).days/365)
    return age

# generate a random date of birth
def dob_gen():
    SLASH = '/'
    month = random.randint(1,12)
    year = random.randint(1970,1995)
    if month == 2 and year % 4 == 0:
        date = random.randint(1,29)
    elif month == 2 and year % 4 != 0:
        date = random.randint(1,28)
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        date = random.randint(1,31)
    else:
        date = random.randint(1,30)
    dob = str(month) + SLASH + str(date) + SLASH + str(year)
    return dob
