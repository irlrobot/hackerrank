#!/bin/python3
# https://www.hackerrank.com/challenges/stockmax/problem
import os


# Complete the stockmax function below.
def stockmax(prices):
    profit = 0
    purchases = []
    remaining_prices = prices[:]
    highest_price = max(prices)

    for index, price in enumerate(prices):
        print(("Pass {} of {}").format(index + 1, len(prices)))
        if index == len(prices) - 1:
            if price == highest_price:
                for _purchase in purchases:
                    print("Selling a share...")
                    profit += price
                    print(profit)
                print("Done selling shares...")
        else:
            if price == highest_price:
                for _purchase in purchases:
                    print("Selling a share...")
                    profit += price
                    print(profit)
                purchases = []

                del remaining_prices[0]
                highest_price = max(remaining_prices)
            else:
                del remaining_prices[0]
                highest_price = max(remaining_prices)

                if price < highest_price:
                    print("Buying a share...")
                    purchases.append(price)
                    profit -= price

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
