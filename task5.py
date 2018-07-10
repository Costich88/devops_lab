#!/usr/bin/python3

# point number 5
# Description: https://www.hackerrank.com/challenges/no-idea/problem


def findint(str):

        return [int(s) for s in str.split()]


def happiness():

        happylevel = 0

        parametres = input('Input default array and disjoint sets sizes:\n')
        n, m = findint(parametres)[0], findint(parametres)[1]

        array = input('Input array values:\n')
        arr = [findint(array)[i] for i in range(n)]

        avalues = input('Input values of the A set:\n')
        A = {findint(avalues)[i] for i in range(m)}

        bvalues = input('Input values of the B set:\n')
        B = {findint(bvalues)[i] for i in range(m)}

        B = ((A ^ B) & B)  # clear matches in B with A

        for i in A:
                if i in arr:
                        happylevel += 1

        for i in B:
                if i in arr:
                        happylevel -= 1
        print(A)
        print(B)

        return happylevel


print(happiness())
