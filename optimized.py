"""Optimized algorithm.

"""

import sys
from math import trunc
from utils import serialize_data_from_csv, calculate_profit


def optimized(value, stocks):
    # Build a matrix of possible solutions
    value = trunc(value)
    m = [[0 for column in range(value + 1)] for line in range(len(stocks) + 1)]

    # Start from index 1 because no solutions in first line and first column
    # Iterate for each line (or for each stock)
    for ln in range(1, len(stocks) + 1):
        # Iterate for each column (or for each value)
        for col in range(1, value + 1):
            if stocks[ln - 1][1] <= col:
                m[ln][col] = max(stocks[ln - 1][2] + m[ln - 1][col - trunc(stocks[ln - 1][1])], m[ln - 1][col])
            else:
                m[ln][col] = m[ln - 1][col]

    v = value
    n = len(stocks)
    picked = []

    while v >= 0 and n >= 0:
        pick = stocks[n - 1]
        if m[n][trunc(v)] == m[n - 1][trunc(v - pick[1])] + pick[2]:
            picked.append(pick)
            v -= pick[1]
        n -= 1
    return m[-1][-1], picked


if __name__ == "__main__":
    stocks = serialize_data_from_csv(sys.argv[1])
    results = optimized(500.56, stocks)
    calculate_profit(results)
