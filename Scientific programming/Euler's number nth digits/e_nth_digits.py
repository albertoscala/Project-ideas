# Go check the creator of this algortihm
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
            e = str(int(round(sum * scaler)))
            return e[0] + '.' + e[1:]

        # Updating counter
        i += 1

        # Updating the factorial
        factorial *= i

# -------------TESTS-------------


def test_5_digits():
    assert e_nth_digits(5) == '2.71828'


def test_10_digits():
    assert e_nth_digits(10) == '2.7182818285'


def test_20_digits():
    assert e_nth_digits(20) == '2.71828182845904523536'


def test_50_digits():
    assert e_nth_digits(50) == '2.71828182845904523536028747135266249775724709369996'


def test_100_digits():
    assert e_nth_digits(100) == '2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274'


# --------------END--------------


if __name__ == '__main__':
    n = int(input('Number of digits: '))
    print(e_nth_digits(n))
