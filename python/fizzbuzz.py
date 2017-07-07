def fizzbuzz(number):
    for i in range(1,number):
        print(str(i) + word(i,3,'Fizz') + word(i,5,'Buzz'))


def word(number, divisor, my_word):
    return my_word if number % divisor == 0 else ""

fizzbuzz(30)
