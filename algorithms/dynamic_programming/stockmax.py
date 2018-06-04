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
    purchases = []
    remaining_prices = prices[:]
    highest_price = max(prices)

    for index, price in enumerate(prices):
        print(("Pass {} of {}").format(index + 1, len(prices)))
        # print(prices)
        # print(profit)
        # print(purchases)
        # print(remaining_prices)
        # print(price)
        # print(highest_price)
        if index == len(prices) - 1:
            # print("Last Price!")
            if price == highest_price:
                # print("Highest price found...")
                for _purchase in purchases:
                    print("Selling a share...")
                    profit += price
                    print(profit)
                print("Done selling shares...")
        else:
            # print("Not last price...")
            if price == highest_price:
                # print("Highest price found...")
                for _purchase in purchases:
                    print("Selling a share...")
                    profit += price
                    print(profit)
                purchases = []
                print("Done selling shares...")

            del remaining_prices[0]
            if any(i > price for i in remaining_prices):
                print("Buying a share...")
                purchases.append(price)
                profit -= price
            # print(("remaining prices {}").format(remaining_prices))
            highest_price = max(remaining_prices)
            # print(("Highest price set to {}").format(highest_price))

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
