#!/usr/bin/python3

# point number 5
# Description: https://www.hackerrank.com/challenges/no-idea/problem


def findint(str):

        return [int(s) for s in str.split()]


def happiness(filename):

        happylevel = 0

        with open(filename) as file:
                array = [row.strip() for row in file]

        parametres = array[0]
        n, m = findint(parametres)[0], findint(parametres)[1]

        arr = [findint(array[1])[i] for i in range(n)]

        A = {findint(array[2])[i] for i in range(m)}

        B = {findint(array[3])[i] for i in range(m)}

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


print(happiness("./input5.txt"))
