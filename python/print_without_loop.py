# Example of using recursion to avoid loops

def print_line(count):
    if count < 1:
        return
    else:
        print('Hello Sridhar')
        print_line(count - 1)


print_line(10)
