

#4.1

class isEven:

    def __init__(self):

        self.count = 0

    def is_Even(self, v):

        if v == 0:
            return (self.count % 2) == 0

        else:
            self.count += 1
            return self.is_Even(v-1)


even = isEven()

#print(even.is_Even(11))

#4.2

class power:

    def calc_power(self, b, n):
        if n == 1:
            return b
        if n % 2 == 0:
            return self.calc_power(b, n/2)**2
        else:
            return (self.calc_power(b, n//2)**(2))*b


exp = power()
#print(exp.calc_power(2,4))

#4.3n

import numpy as np

class MatrixPower:
    def __init__(self):

        self.matrix = np.matrix('1, 1; 1, 0')

    def to_power(self, n):

        if n == 1:
            return self.matrix
        else:
            return np.matmul(self.matrix, self.to_power(n-1))


pow = MatrixPower()

# print(pow.to_power(3))


#4.4


class slowProduct:

    def slow_multiply(self, n, m):

        if n == 1:
            return m

        else:
            return self.slow_multiply(n-1, m) + m


product = slowProduct()

# print(product.slow_multiply(3, 4))


#4.5

import decimal

class efficientSlowProduct():

    def __init__(self):
        self.producttracker = 0


    def less_slow_multiply(self, n, m):

        if m < 2:
            return n * m

        if n < 2:
            return n * m

        elif n % 2 ==0 and m % 2 == 0:
            return self.less_slow_multiply(n/2, m/2)*4

        elif n % 2 is not 0 and m % 2 is not 0:
            return (self.less_slow_multiply(n/2, m/2))*4

        elif n % 2 is not 0:
            return (self.less_slow_multiply(n/2, m/2))*4

        elif m % 2 is not 0:
            return (self.less_slow_multiply(n/2, m/2))*4


sp = efficientSlowProduct()

# print(sp.less_slow_multiply(15, 4))


#4.6

class callbackSum:
    def __init__(self, m, n, cb):

        self.m = m
        self.n = n
        self.cb = cb

        print(self.compute_sum(cb))

    def compute_sum(self, cb):

        if self.m == self.n:
            return 0
        else:
            self.m +=1
            return cb(self.m) + self.compute_sum(cb)

def timesTwo(a):
    return a*2

# callbackSum(0,5, timesTwo)


#4.7

class digitCounter:
    def __init__(self, number):

        self.number = number
        self.count = 0

    def countDigit(self):

        if self.number == 0:
            return self.count
        else:
            self.number = self.number // 10
            self.count +=1
            return self.countDigit()

# counter = digitCounter(126634)
#
# print(counter.countDigit())

#4.8


class binaryToDecimal:
    def __init__(self, binary):

        self.binary = binary
        self.decimal = 0
        self.placeCounter = 1

    def convertToDecimal(self):

        if self.binary == 0:
            return self.decimal
        digit = self.binary % 10
        self.decimal += digit * self.placeCounter
        self.placeCounter *= 2
        self.binary = self.binary // 10
        return self.convertToDecimal()

dec = binaryToDecimal(1010)

# print(dec.convertToDecimal())