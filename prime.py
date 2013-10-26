import sys
import re

def is_prime(num):
    """
    >>> is_prime(5)
    True
    >>> is_prime(4)
    False
    """
    pass

if __name__ == '__main__':
    for i in range(1,len(sys.argv)):
        num = sys.argv[i]
        if is_prime(num):
            print("{} is prime!".format(num))
        else:
            print("{} is not prime!".format(num))
