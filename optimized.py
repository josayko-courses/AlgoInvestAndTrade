"""Optimized algorithm.

"""

import sys
from utils import serialize_data_from_csv, calculate_profit


def optimized(value, stocks):
    return


if __name__ == "main":
    stocks = serialize_data_from_csv(sys.argv[1])
    results = optimized(500, stocks)
    calculate_profit(results)
