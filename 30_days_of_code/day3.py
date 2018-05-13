#!/bin/python3

import math
import os
import random
import re
import sys

def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    N = int(input())
    
    if is_even(N):
        if N in range(2, 6):
            print('Not Weird')
        if N in range(6, 21):
            print('Weird')
        if N > 20:
            print('Not Weird')
    else:
        print('Weird')
