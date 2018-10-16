#!/bin/python3
import math
import os
import random
import re
import sys

def print_multiples_of(num):
    x = 1
    while x < 11:
        total = num * x
        print("{} x {} = {}".format(num, x, total))
        x += 1

if __name__ == '__main__':
    n = int(input())
    print_multiples_of(n)
