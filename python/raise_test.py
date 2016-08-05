def testing_raise(number):
    if number == 0:
        raise Exception('cannot continue further')
    try:
        if number == 4:
            raise ValueError('4 is passed')
    except ValueError as ve:
        print('got it ', ve)

    else:
        print(number)


testing_raise(4)
testing_raise(0)
testing_raise(5)
