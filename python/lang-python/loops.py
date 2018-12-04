#!/bin/python3
"""
https://www.hackerrank.com/challenges/python-loops/problem
Read an integer N. For all non-negative integers i < N, print i^2. 
See the sample for details.
"""


if __name__ == '__main__':
    n = int(input())

    if n >= 0:
        i = 0
        while i < n:
            print(i**2)
            i += 1
