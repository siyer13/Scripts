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
    print(phonenumber)
    return phonenumber
