# This is where you will write your awesome calculator.

def calc_fizzbuzz(n):
    if n % 15 == 0:
        return 'FizzBuzz'
    elif n % 5 == 0:
        return 'Buzz'
    elif n % 3 == 0:
        return 'Fizz'
    else:
        return str(n)


def loop():
    num = input('Enter a number: ')
    print(calc_fizzbuzz(int(num)))


if __name__ == '__main__':
    while True:
        loop()
