import itertools

# Below program generates all the possible numbers that can be generated from
# a given number


# function to create the list of digits from a given number
def make_digits(number):
    digit_list = []
    while number > 0:
        quotient = int(number / 10)
        remainder = number % 10
        number = quotient
        digit_list.append(remainder)
    return digit_list

# function that actually generates number from tuples
def  generate_number(num_set):
    number = 0
    power = len(num_set) - 1
    for digit in num_set:
        if power == 0:
            number = number + digit
        else:
            number = digit * pow(10,power) + number
            power = power - 1
    return number

# function to create numbers for list of digit tuples
def make_number(digit_list):
    perm_num_list = []
    for num_set in digit_list:
        number = generate_number(num_set)
        perm_num_list.append(number)
    return perm_num_list

given_list = make_digits(9545)
list_of_permuation = list (itertools.permutations(given_list))
output_list = make_number(list_of_permuation)
print(output_list)
