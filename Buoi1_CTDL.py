### Russian Doll ###

#def openRussianDoll(doll):
#    if doll == 1:
#        print("All dolls are opened")
#    else:
#        openRussianDoll(doll-1)

#openRussianDoll(4)
"""
### firstMethod ###
def firstMethod():
    secondMethod()
    print("I am the first Method")

def secondMethod():
    thirdMethod()
    print("I am the second Method")

def thirdMethod():
    fourthMethod()
    print("I am the third Method")

def fourthMethod():
    print("I am the fourth Method")


firstMethod()
"""
"""
### recursiveMethod ###
def recursiveMethod(n):
    if n<1:
        print("n is less than 1")
    else: 
        recursiveMethod(n-1)
        print(n)

recursiveMethod(4)
"""
"""
### powerOfTwo ###
def powerOfTwo(n):
    if n == 0:
         return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2

print(powerOfTwo(3))
"""
"""
### Giai thua ###
def factorial(n):
    assert n >= 0 and int(n) == n
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))
"""

### Fibonacci ###
def fibonacci(n):
    assert n >=0 and int(n) == n
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))

"""
### How to find the sum of digits of a positive integer number using recursion ? ###
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)
print(sum_digits(190302))
"""
"""
### How to calculate power of a number using recursion? ###
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
print(power(3,3))
"""
"""
### How to find GCD ( Greatest Common Divisor) of two numbers using recursion? ###
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(12,18))
"""
"""
### How to convert a number from Decimal to Binary using recursion ? ###
def decimal_to_binary(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(n // 2)
print(decimal_to_binary(19))
"""
