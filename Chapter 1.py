
#Chapter 1


#1.1

answer = "N!"

#1.2

"""When s0 = 0"""
s1 = 3
s1 = 6
s2 = 9
s3 = 12

"""When s0 = 4"""

s1 = 7
s2 = 10
s3 = 13
s4 = 16

answer = "Both cases are an arithmetic sequence where r = 3."


#1.3


answer = "If given si and sj, a series of linear equations can be created. These can be solved for the intermediary" \
         "values of s." \

# s2 = 1 + s0
#
# s3 = (1+s0) + 1
#
# s4 = [(1+s0) + 1] + [1 + s0]
#
# s5 = 17 = [(1+s0) + 1] + [1 + s0] + [(1+s0) + 1]
#
# 17 = 3s0 + 5
#
# s0 = 4


#1.4

answer = "D(P) = { 0                if C(P) == 0" \
         "         C(P) + D(C(P))   if C(P) > 0 "


#1.5

answer = "F(n) = F(n-1) + F(n-2). Let n = 5, then F(5) = F(4) + F(3) = F(3) + F(2) + F(3) = F(2) + F(1) + F(2) + F(3). " \
         "In the alternative form, F(5) = F(2) + F(1) + F(2) + F(3). Thus, the two forms are equal." \

#1.6


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)


#1.7

def sum_list_length2(a):
    if a == []:
        return 0
    else:
        return a.pop(0) + sum_list_length2(a)


#1.8

def sum_from_end(a, n):
    if n == 0:
        return 0
    return sum_from_end(a, n-1) + a[n-1]


def sum_from_beginning(a, n):

    if n == 0:
        return 0
    return a[0] + sum_from_beginning(a[1:], n-1)

def sum_from_middle(a, n):

    if n == 1:
        return a[0]
    else:
        return sum_from_middle(a[:n//2], n//2) + sum_from_middle(a[n//2:], n-n//2)


#1.9


# let S(n-1) = (x^n - 1)/(x-1). Then, S(n) = (x^(N+1) - 1)/(x-1)
#
# Summation x^i. Then (x^n - 1)/(x-1) + x^(n) = (x^(N+1) - 1)/(x-1); x^n -1 + x^(n+1) - x^n = x^(N+1) - 1, which completes the proof.


#1.10


