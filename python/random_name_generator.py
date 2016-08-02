import random
import os

data = open(r"C:\Users\python\names.txt").readlines()
print(random.choice(data))
print(random.randint(20,50))
