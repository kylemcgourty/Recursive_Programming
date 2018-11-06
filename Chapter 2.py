

#2.1

answer = "The size of problem in the length of the binary representation of the number. Size in len(input)."


#2.2

answer = "See S(n)"
"""
       0 if n = 0     
S(n) = S(n-1) + n if n > 0  """

count1 = 0
def addFirst_N_Numbers(n):


    if n == 0:
        return 0
    else:
        return addFirst_N_Numbers(n-1) + n



#2.3

def addFirst_N_Numbers_via_Division(n):
    if n == 0:

        return 0
    if n == 1:

        return 1
    else:
        if n % 2 == 0:
            return 3*addFirst_N_Numbers_via_Division(n/2) + addFirst_N_Numbers_via_Division(n/2-1)
        else:
            return 3*addFirst_N_Numbers_via_Division((n-1)/2) + addFirst_N_Numbers_via_Division((n+1)/2)




#2.4.

answer = "The base case exists when there is an input of length 1. A recursive diagram:" \
         """
         d0d1d2d3                    d0d1d2d3
         
         remove most sig digit         + d0
         
         d1d2d3                        d1d2d3
         """


def digitPrinter(number):

    if number < 10:
        print(number)
        return

    digit = number // (10 ** (len(str(number))-1)) % 10
    print(digit)

    remaining = number % (10 ** (len(str(number))-1))

    digitPrinter(remaining)


# digitPrinter(1986)


#2.5

answer = "A divide and conquer approach to finding the largest digit"


""" 
    Array of size n                                         S(array)
    
                                                                
    
    
    array[:len(array)/2]   when n = 1, compare to largest    S(array[:len(array)/2]


"""

#2.6

class calcLargest:
    def __init__(self):
        self.largest  = 0;


    def findLargest(self, collection):

        if len(collection) == 0:
            return self.largest

        if collection[0] > self.largest:
            self.largest = collection[0]

        self.findLargest(collection[1:])

        return self.largest;



