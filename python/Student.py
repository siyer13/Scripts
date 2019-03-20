from datetime import datetime


class Student:

    def __init__(self, name, dob='', age=0):
        self.name = name
        self.dob = dob
        self.age = age

    @classmethod
    def find_age(cls, dob):
        dob = datetime.strptime(dob, '%d-%b-%Y')
        age = datetime.now().year - dob.year
        print(age)
        age = cls.age
        #cls(dob, age)
        #print(cls.is_adult(age))
        #return cls(dob, age)

    @staticmethod
    def is_adult(age):
        if age < 18:
            raise Exception()



stu = Student('Sri')
print(stu.find_age('13-DEC-1996'))
print(stu.age, stu.dob, stu.name)
