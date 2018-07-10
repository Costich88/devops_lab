#!/usr/bin/python3

# The task abount a painter


def fint(str):

        return [int(s) for s in str.split()]


def paintersquare():

        ps = input('Input default sizes:\n')
        square = fint(ps)[0] * fint(ps)[1]

        n = int(input('Input number of rectangles:\n'))

        sarr = [[0 for j in range(fint(ps)[0])] for i in range(fint(ps)[1])]

        for i in range(n):
            psn = input('Input points of rectangle {0}:\n'.format(i + 1))
            for j in range(fint(psn)[0], fint(psn)[2]):
                for k in range(fint(psn)[1], fint(psn)[3]):
                    sarr[j][k] = 1

        sum = 0

        for arr in sarr:
                for el in arr:
                        sum += el
        square -= sum
        return square


print(paintersquare())
