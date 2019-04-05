def delim(input_str):
    lst = []
    word = ''
    delimiter_char = ','
    for ch in input_str:
        if ch == delimiter_char:
            lst.append(word.strip())
            word = ''
        else:
            word = word + ch
    lst.append(word)
    print(len(lst))
    return lst

print(delim('hello, this is , my string, haha'))
