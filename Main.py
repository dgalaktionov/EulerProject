# -*- coding: utf-8 -*-

'''
Created on 07/07/2014

@author: DaGal
'''

import math

'''
    Sums all the multiples of k below n.
'''
def sum_mult(k, n):
    i = int((n - 1) / k)
    return int(k * (i + 1) * i / 2)

'''
    Sums the even-valued terms of fibonacci, until n value.
'''
def sum_fibo(n):
    i = 1
    j = 2
    p = i
    s = 0

    while (j < n):
        s += j
        i += j  # 3
        j += i  # 5
        i += j  # 8

        p = i
        s += p

        j += i  # 13
        i += j  # 21
        j += i  # 34

    if (p >= n):
        s -= p

    return s

'''
    Finds the largest prime factor of n.
'''
def find_lpf(n):
    while(n % 2 == 0):
        n /= 2

    if (n < 2):
        return 2

    i = 3
    while (i != n):
        while (n % i == 0):
            n /= i

        i += 2

    return i

'''
    Check if n is a palindrome.
'''
def check_palindrome(n):
    return str(n) == str(n)[::-1]


'''
    Finds the largest palindrome from the product of n-digit numbers.
'''
def find_lp(n):
    p = 0

    for i in range(10 ** (n - 1), 10 ** n):
        for j in range(i, 10 ** n):
            if check_palindrome(i * j) and i * j > p:
                p = i * j

    return p

'''
    Difference between the sum of the squares of the first n numbers and the square of the sum.
'''
def ssq_dif(n):
    sum_of_squares = 1
    s = int((n + 1) * n / 2)

    for i in range(2, n + 1):
        sum_of_squares += i * i

    return s * s - sum_of_squares

'''
    Check if n is prime against the list of n primes
'''
def is_prime(n, primes):
    for p in primes:
        if n % p == 0:
            return False

    return True

'''
    Find the n-th prime.
'''
def get_prime(n):
    primes = [3]  # ignore 2 and its multiples :-)
    i = 5
    j = 2

    while j < n:
        if is_prime(i, primes):
            primes.append(i)
            j += 1
        i += 2

    return primes[-1]

'''
    Find the greatest n-adjacent numbers that give the biggest product
'''
def greatest_adjacent_mult(n):
    bignum = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984\
80186947885184385861560789112949495459501737958331952853208805511125406987471585238630507156932\
90963295227443043557668966489504452445231617318564030987111217223831136222989342338030813533627\
66142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797\
90879227492190169972088809377665727333001053367881220235421809751254540594752243525849077116705\
56013604839586446706324415722155397536978179778461740649551492908625693219784686224828397224137\
56570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427\
17147992444292823086346567481391912316282458617866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408071984038509624554443629812309878799272442849\
09188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005\
593572972571636269561882670428252483600823257530420752963450"
    multiples = bignum[0:n]
    i = 0
    digits = len(bignum)
    max_prod = 0
    prod = 1

    while i + n <= digits:
        multiples = bignum[i:i + n]
        prod = 1

        for j in multiples:
            prod *= int(j)

        if prod > max_prod:
            max_prod = prod

        i += 1

    return max_prod

'''
    Find the product of the pythagorean triplet whose sum is n.
'''
def pythagorean_from_sum(n):
    a = 1
    b = 2
    c = n - 3

    while b < c:
        while b < c:
            if a * a + b * b == c * c:
                return a * b * c

            c -= 1
            b += 1

        a += 1
        b = a + 1
        c = n - a - b

    return 0

'''
    Eratostenes cribe of n
'''
def cribe(n):
    numbers = [True] * n

    for i in range (2, int(math.sqrt(n))):
        if numbers[i]:
            j = i * 2

            while (j < n):
                numbers[j] = False
                j += i

    return numbers


'''
    Return the sum of all the primes below n.
'''
def sum_of_primes(n):
    c = cribe(n)
    s = 0

    for i in range(0, len(c)):
        if c[i]:
            s += i

    return s - 1


def prob1():
    print sum_mult(3, 1000) + sum_mult(5, 1000) - sum_mult(15, 1000)

def prob2():
    print sum_fibo(4000000)

def prob3():
    print find_lpf(600851475143)

def prob4():
    print find_lp(3)

def prob5():
    print 2 * 3 * 2 * 5 * 7 * 2 * 3 * 11 * 13 * 2 * 17 * 19

def prob6():
    print ssq_dif(100)

def prob7():
    print get_prime(10001)

def prob8():
    print greatest_adjacent_mult(13)

def prob9():
    print pythagorean_from_sum(1000)

def prob10():
    print sum_of_primes(2000000)

problems = [None,
None,
lambda: prob2(),
lambda: prob3()]

def main():
    prob10()

if __name__ == '__main__':
    main()
