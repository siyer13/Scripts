def unique_character_string(string_value):
    char_set = []
    for i in string_value:
        if char_set[i]:
            return False
        char_set[i] = True
    return True

print(unique_character_string('abcd'))
