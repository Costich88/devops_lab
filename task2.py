#!/usr/bin/python3

# Checks, if the input string is palindrome


def palindrome(string):

        pal = True

        for i in range(len(string) // 2):

                if string[i] != string[len(string) - i - 1]:

                        pal = False
                        break
        return pal


string = input()
print(palindrome(string))
