def type(letter, key):
    string = ""
    for i in range(key):
        string = string + letter
    return string

def compressstring(given_string):
    print("Given String: ", given_string)
    present_character_count = [given_string[0],1]
    letter_count_map = [present_character_count]
    for c in given_string[1:]:
        if c == present_character_count[0]:
            present_character_count[1] += 1
        else:
            present_character_count = [c, 1]
            letter_count_map.append(present_character_count)
    output_string = ""
    for keys in letter_count_map:
            count = 0;
            for key in keys:
                count = count + 1
                if count == 1:
                    letter = key
                if count == 2:
                    if key > 3:
                        output_string = output_string + str(key) +"X" + letter
                    else:
                        output_string = output_string + type(letter, key)

    return output_string


print("Compressed String: " ,compressstring('aaaaaaabbbccccccddaaddddddddddddddBBBggggggggggggggggg'))
