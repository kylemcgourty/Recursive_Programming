

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


