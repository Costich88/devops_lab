#!/usr/bin/python3

# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order


def reverseWords(s):
        array = s.split()
        for n in range(len(array)):
                arrayn = [i for i in array[n]]
                arrayn.reverse()
                array[n] = ''
                array[n] = ''.join(arrayn)
                s = ' '.join(array)
                return s


print(reverseWords("Let's take LeetCode contest"))
