#!/usr/bin/python3
# Given an integer n, print the following values for each
# integer from 1 to n: Decimal, Octal, Hexadecimal (capitalized), Binary

n = int(input())

for i in range(1, n+1):
        print(str(i).center(len(bin(n))-2), end=' ')
        print(str(oct(i)[2:]).center(len(bin(n))-2), end=' ')
        print(str(hex(i)[2:].upper()).center(len(bin(n))-2), end=' ')
        print(str(bin(i)[2:]).center(len(bin(n))-2))
