"""
Написать два алгоритма нахождения i-го по счёту простого числа.
"""
import cProfile
from math import log


def test1():
    from sympy import prime
    print(prime(458988))


def test2():
    def prime_range(number):
        n = 100
        while number > n / log(n):
            n += 1000
        return n

    def sieve_eratosthenes(k):
        n = prime_range(k)
        numbers = list(range(2, n+1))
        for number in numbers:
            if number != 0:
                for candidate in range(2 * number, n+1, number):
                    numbers[candidate-2] = 0
        primes = list(filter(lambda x: x != 0, numbers))
        if len(primes) > k:
            print(primes[k-1])
            return primes[k-1]
        return 0

    sieve_eratosthenes(458988)


def main():
    test1()
    test2()


cProfile.run('main()')

#      1    0.047    0.047    4.245    4.245 task2.py:13(test2) - второй вариант
#       1    0.002    0.002    0.002    0.002 task2.py:14(prime_range)
#       1    3.566    3.566    4.197    4.197 task2.py:20(sieve_eratosthenes)
# 7251099    0.629    0.000    0.629    0.000 task2.py:27(<lambda>)
#       1    0.000    0.000    4.986    4.986 task2.py:36(main)
#       1    0.000    0.000    0.741    0.741 task2.py:8(test1) - первый вариант
