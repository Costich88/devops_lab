#!/usr/bin/python3

# The task abount a painter


def fint(str):

        return [int(s) for s in str.split()]


def paintersquare(filename):

        with open(filename) as file:
            array = [row.strip() for row in file]

        ps = array[0]
        square = fint(ps)[0]*fint(ps)[1]

        n = fint(array[1])[0]

        sarr = [[0 for j in range(fint(ps)[0])] for i in range(fint(ps)[1])]

        for i in range(n):
            for j in range(fint(array[i+2])[0], fint(array[i+2])[2]):
                for k in range(fint(array[i+2])[1], fint(array[i+2])[3]):
                                sarr[j][k] = 1

        sum = 0

        for arr in sarr:
                for el in arr:
                        sum += el
        square -= sum
        return square


print(paintersquare("./INPUT.txt"))

with open("OUTPUT.txt", "w") as text_file:
    print(paintersquare("./INPUT.txt"), file=text_file)
