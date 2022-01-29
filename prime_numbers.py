def is_prime(number):
    if number > 1:
        for n in range(2, number):
            if (number % n) == 0:
                return print(number, 'is not a prime number!')
        else:
            return print(number, 'is a prime number!')

    else:
        return print(number, 'is not a prime number!')


num = int(input('Enter a number: '))
is_prime(num)
