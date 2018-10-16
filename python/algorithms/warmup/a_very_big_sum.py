#!/bin/python3
import os
import sys
#
# Complete the aVeryBigSum function below.
#
def a_very_big_sum(n, ar):
    total = 0
    for num in ar:
        total += num
    return total

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = a_very_big_sum(n, ar)
    f.write(str(result) + '\n')
    f.close()
