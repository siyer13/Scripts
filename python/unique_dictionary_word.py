# Given multiple strings like "candy", "carry", "dummy", etc.
# These strings are stored as c3y, c3y and d3y etc.
# Write a function which returns a boolean
# if the string (like "carry" is unique in the dictionary)


# str = 'carry'
# print(str[:1])
# print(len(str))
# print(str[-1:])


list_of_strings = ['carry','dummy','funny','ceray']
new_list_of_strings = []
map_of_strings = {}

# The below function returns True if the word alreday exists
# else it returns false
def unique_word(new_word):
    if map_of_strings.__contains__(new_word):
        return True
    else:
        map_of_strings.update({new_word : ""})
        return False


for word in list_of_strings:
    first_char = word[:1]
    no_of_middle_chars = len(word) - 2
    last_char = word[-1:]
    new_word = first_char + str(no_of_middle_chars) + last_char
    new_list_of_strings.append(new_word)
      print(unique_word(new_word))
