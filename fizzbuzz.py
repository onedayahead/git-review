# This is where you will write your awesome calculator.
import atexit

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
    try:
        n = int(num)
        print(calc_fizzbuzz(n))
    except ValueError:
        pass


if __name__ == '__main__':
    def quit_gracefully():
        print 'Bye'

    atexit.register(quit_gracefully)

    while True:
        try:
            loop()
        except EOFError:
            break
