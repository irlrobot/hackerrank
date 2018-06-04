#!/bin/python3
# https://www.hackerrank.com/challenges/stockmax/problem
import os


# Complete the stockmax function below.
def stockmax(prices):
    profit = 0
    remaining_prices = prices[:]
    highest_price = max(remaining_prices)

    for price in prices:
        del remaining_prices[0]
        try:
            highest_price = max(remaining_prices)
        except ValueError:
            break
        if price < highest_price:
            profit += (highest_price - price)

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
