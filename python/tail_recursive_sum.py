def tail_recursive_sum(sum,number):
    if number < 1:
        return sum
    else:
        sum = sum + number
        return tail_recursive_sum(sum, number -1)

print(tail_recursive_sum(0,5))
