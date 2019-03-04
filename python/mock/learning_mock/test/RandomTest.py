from unittest import TestCase, mock, main
from services.Random import is_even_odd


class RandomTest(TestCase):

    @mock.patch('services.Random.randint')
    def test_random_even(self, randint_mock):
        randint_mock.return_value = 40
        even_rand_num = is_even_odd()
        print(even_rand_num)
        self.assertEqual('Number 40 is even', even_rand_num)

    @mock.patch('services.Random.randint')
    def test_random_odd(self, randint_mock):
        randint_mock.return_value = 39
        odd_rand_num = is_even_odd()
        print(odd_rand_num)
        self.assertEqual('Number 39 is odd', odd_rand_num)


if __name__ == '__main__':
    main()
