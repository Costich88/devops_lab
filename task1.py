#!/usr/bin/python3

# Reads an integer N, for all non-negative i<N prints i**2

N = input()
listl = [i**2 for i in range(int(N))]
print(listl)
