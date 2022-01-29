def print_factors(num):
    for n in range(1, (num + 1)):
            if (num % n) == 0:
                print(n)

num = int(input('Enter a number: '))
print_factors(num)
