#!/bin/python3
# https://www.hackerrank.com/challenges/stockmax/problem
import math
import os
import random
import re
import sys


# Complete the stockmax function below.
def stockmax(prices):
    profit = 0
    highest_price = max(prices)
    purchases = []

    for price in prices:
        if price < highest_price:
            purchases.append(price)
            print(purchases)
            profit -= price
            print(profit)
        if price == highest_price:
            for index, purchase in enumerate(purchases):
                profit += purchase
                del purchases[index]

    return profit


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()