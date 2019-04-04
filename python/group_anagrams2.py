
def allAnagram(input):

    f_dict = {}

    for str_val in input:
        key = ''.join(sorted(str_val))
        if key in f_dict.keys():
            f_dict[key].append(str_val)
        else:
            f_dict[key] = []
            f_dict[key].append(str_val)
    print(f_dict.values())




if __name__ == "__main__":
    input=['cat', 'dog', 'tac', 'god', 'act']
    allAnagram(input)
