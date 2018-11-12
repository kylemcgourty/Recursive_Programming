

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
            return self.less_slow_multiply(n/2, m/2)

        elif n % 2 is not 0 and m % 2 is not 0:
            return (self.less_slow_multiply(n/2, m/2))*4

        elif n % 2 is not 0:
            return (self.less_slow_multiply(n/2, m/2))*4

        elif m % 2 is not 0:
            return (self.less_slow_multiply(n/2, m/2))*4


sp = efficientSlowProduct()

print(sp.less_slow_multiply(15, 4))