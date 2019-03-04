from random import randint


def is_even_odd():

    number = randint(1, 100)
    if number % 2 == 0:
        print('Number {} is even'.format(number))
        return 'Number {} is even'.format(number)
    else:
        print('Number {} is odd'.format(number))
        return 'Number {} is odd'.format(number)


if __name__ == '__main__':
    is_even_odd()
