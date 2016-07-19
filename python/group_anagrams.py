# Given a set of random strings,
# write a function that returns a set that groups all the anagrams together.
# Ex: star, dog, car, rats, ars - > {(star, rats), (src,car), dog)

from collections import defaultdict
import hashlib

given_list = ['dog','car','rats','ars','star']


# Here's my solution,
# 1. Create a dictionary to hold list of values
# 2. Sort each word in the list alphabetically
# 3. Generate a hash for the sorted word
# 4. Insert into map the generated hash as key and the original word as values

# Program
def group_anagrams(given_list):
    hash_dict = defaultdict(list)
    # sort each word
    for word in given_list:
        sorted_word = ''.join(sorted(word))
        # generate hash for that sorted word
        hash_num = hashlib.md5(sorted_word.encode(encoding='utf_8')).hexdigest()
        # Insert hash_num as key and word as value in hash_dict
        hash_dict[hash_num].append(word)
    return hash_dict.values()


print(group_anagrams(given_list))
