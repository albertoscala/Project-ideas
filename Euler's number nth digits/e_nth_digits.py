# https://www.nayuki.io/page/approximating-eulers-number-correctly

from fractions import Fraction


def e_nth_digits(n):

    sum = Fraction(0)
    factorial = 1

    # Error target
    error = 10 ** n

    # Constant to remove the floating point
    scaler = Fraction(error)

    # Counter for the factorial
    i = 0

    while True:

        # Term I of the partial sum
        term = Fraction(1, factorial)

        # Partial sum to get e
        sum += term

        # If term den > targer error equals to 1/f < 1/error (10^-m)
        if factorial > error:
            e = str(int(sum * scaler))
            return e[0] + '.' + e[1:]

        # Updating counter
        i += 1

        # Updating the factorial
        factorial *= i


if __name__ == '__main__':
    n = int(input('Number of digits: '))
    print(e_nth_digits(n))
