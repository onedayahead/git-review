# This is where you will write your awesome calculator.

def calc_fizzbuzz(n):
    if not isinstance(n, int):
        raise ValueError('Must provide an integer to calc_fizzbuzz')

    if n % 15 == 0:
        return 'FizzBuzz'
    elif n % 5 == 0:
        return 'Buzz'
    elif n % 3 == 0:
        return 'Fizz'
    else:
        return str(n)


def loop():
    num = raw_input('Enter a number: ')
    try:
        n = int(num)
        print(calc_fizzbuzz(n))
    except ValueError:
        pass

if __name__ == '__main__':
    while True:
        loop()
