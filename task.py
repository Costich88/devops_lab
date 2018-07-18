#!/usr/bin/python3

# The task abount a painter


def fint(str):

        return [int(s) for s in str.split()]


def findsquare(width, lengh):

        return width * lengh


def squarearray(width, lengh):

        return [[0 for j in range(lengh)] for i in range(width)]


def cutsqaure(point1, point2, point3, point4, sarr):

        for j in range(point1, point3):

                for k in range(point2, point4):

                        sarr[j][k] = 1

        return sarr


def totcutted(sarr):

        total = 0

        for arr in sarr:
                for el in arr:
                        total += el

        return total


def paintersquare(ps, pnts):

        square = findsquare(fint(ps)[0], fint(ps)[1])

        sarr = squarearray((fint(ps)[0]), (fint(ps)[1]))

        for strval in pnts:
            cutsqaure(fint(strval)[0], fint(strval)[1],
                      fint(strval)[2], fint(strval)[3], sarr)

        total = totcutted(sarr)
        square -= total
        return square


print(paintersquare('5 5', ['1 1 3 3', '2 2 4 4']))
