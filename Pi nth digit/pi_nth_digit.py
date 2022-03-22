from math import factorial
from decimal import Decimal, getcontext

getcontext().prec = 1000

def pi_nth_alg(n):
    # Declaring PI as a decimal for a better precision
    pi = Decimal()

    # Using the formula for N+2 times to obtain PI
    for i in range(n+2):
        div = Decimal(((-1) ** i) * (factorial(6 * i)) * (13591409 + 545140134 * i))
        den = Decimal((factorial(3 * i)) * (factorial(i) ** 3) * (640320 ** (3 * i)))
        pi += div / den

    # Adding the costants
    pi = pi * 12 / Decimal(640320 ** 1.5)

    # Reversing the PI
    pi = 1 / pi

    # Converting the PI to string to get the N digit
    pi = str(pi)

    # Returning PI's N digit
    return pi[n]

if __name__ == '__main__':
    n = int(input('Insert n position of the digit: '))
    print(pi_nth_alg(n))
