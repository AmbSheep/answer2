#!/usr/bin/env python3
import sys

def solutions(amount):
    coins = [1, 3, 5]
    ways = [1] + [0] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]
    return ways[amount]


if __name__ == '__main__':
    print(solutions(int(sys.argv[1])))
