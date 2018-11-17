

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



#4.9

"""recursive_case = 10 * recursive_call(n//b, b) + (n%b)"""


#4.10


class LeastSignificatBit:
    def __init__(self):
        self.count = 1


    def determineBitPosition(self, binary):

        bit = binary % 10

        if bit == 1:
            return self.count
        else:
            self.count +=1
            return self.determineBitPosition(binary/10)


position = LeastSignificatBit()

# print(position.determineBitPosition(1001000))

#4.12


class VowelsInString:
    def __init__(self):
        self.count = 0

    def vowelCounter(self, key):

        if len(key) == 0:
            return self.count

        character = key[0:1]

        if character in ["a", "e", "i", "o", "u", "y"]:
            self.count += 1

        return self.vowelCounter(key[1:])


vowels = VowelsInString()

# print(vowels.vowelCounter("hippopotamus"))


#4.13

class BinomialCoefficient:
    def nChooseR(self, n, r, v):

            return (n * self.factorial(n-1))/(r * self.factorial(r-1)*v*self.factorial(v-1))

    def factorial(self, n):
        if n == 1:
            return 1
        else:
            return n * self.factorial(n-1)



binomial = BinomialCoefficient()
# print(binomial.nChooseR(5, 3, 5-3))


#4.14


class Pascal:
    def __init__(self):
        self.next_row = list()

    def determineNextRow(self, a):

        if len(a) == 1:
            self.next_row.append(1)
            self.next_row.insert(0,1)
            return self.next_row

        self.next_row.append(a[0]+a[1])

        return self.determineNextRow(a[1:])

pascal_triangle = Pascal()

# print(pascal_triangle.determineNextRow([1,4,6,4,1]))


#4.15

class CorrectInsert:
    def __init__(self, original_number):
        self.original_number = str(original_number)
        self.position = 1

    def placeInsert(self, examined_number, digit):

        number_as_string = str(examined_number)
        first_digit = number_as_string[0:1]
        second_digit = number_as_string[1:2]

        if int(first_digit) < digit < int(second_digit):
               return int(self.original_number[:self.position] + str(digit) + self.original_number[self.position:])
        else:
            self.position += 1
            cleaved_number = number_as_string[1:]
            return self.placeInsert(int(cleaved_number), digit)

digit_insert = CorrectInsert(112445799)

# print(digit_insert.placeInsert(112445799, 6))


#4.17


class InsertionSort:

    def __init__(self, a):
        self.a = a

    def sort(self, index):

        if index == len(self.a):
            return self.a
        if index > 0:
            digit = self.a.pop(index)
            if index == len(self.a)-1:
                self.insertionLoop(index-1, digit)
            else:
                self.insertionLoop(index, digit)

        return self.sort(index + 1)

    def insertionLoop(self, index, digit):
        for i in range(index):
            if self.a[i] < digit <= self.a[i+1]:
                self.a.insert(i+1, digit)
                break
            if digit > self.a[index-1]:
                self.a.insert(index, digit)
                break
            if digit <= self.a[0]:
                self.a.insert(0, digit)
                break

insert_sort = InsertionSort([4,2,1,6,8,3,2,1])

print(insert_sort.sort(0))