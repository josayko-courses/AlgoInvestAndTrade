"""Optimized algorithm.

"""

import sys
from math import trunc
from utils import serialize_data_from_csv, calculate_profit


def optimized(value, stocks):
    """Builds and evaluates a matrix of possible solutions to avoid redundant computations.
    The best solution will be in last column of the last line or m[-1][-1].
    """
    # Build a matrix of possible solutions
    value = trunc(value)
    m = [[0 for column in range(value + 1)] for line in range(len(stocks) + 1)]

    # Start from index 1 because no solutions in first line and first column (fill with 0's)
    # Iterate for each stock
    for ln in range(1, len(stocks) + 1):
        # Iterate for each possible value
        for col in range(1, value + 1):
            # if stock price is less or equals to actual value, pick it
            # otherwise skip it, optimized profits is same as previous stock
            if stocks[ln - 1][1] <= col:
                # compare optimized profits of actual value for previous stock with
                # (stock profit + optimized profits for previous stock of [value = actual value - stock value])
                m[ln][col] = max(stocks[ln - 1][2] + m[ln - 1][col - trunc(stocks[ln - 1][1])], m[ln - 1][col])
            else:
                m[ln][col] = m[ln - 1][col]

    v = value
    n = len(stocks)
    picked = []

    # Retrieve picked stocks from the last stock in the matrix until value is zero
    while v >= 0 and n >= 0:
        p = stocks[n - 1]
        # Optimized profit is equals to stock profit + optimized profits for previous stock of [value = actual value - stock value]
        if m[n][trunc(v)] == m[n - 1][trunc(v - p[1])] + p[2]:
            picked.append(p)
            v -= p[1]
        n -= 1
    return m[-1][-1], picked


if __name__ == "__main__":
    if len(sys.argv) > 1:
        stocks = serialize_data_from_csv(sys.argv[1])
        results = optimized(500, stocks)
        calculate_profit(results)
