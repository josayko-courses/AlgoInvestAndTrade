"""Bruteforce algorithm.

"""
import sys
from utils import serialize_data_from_csv, calculate_profit


def bruteforce(value, stocks, picked=[]):
    """Try all possible combinations recursively to get the best profit return.
    The algorithm start from the last element:
    combi1 -> skip it
    combi2 -> pick it
    Args:
        - value: maximum possible value of a combination
        - stocks: a list of tuples representing the stocks -> stocks = [(name, price, profit)]
        - picked: a list of the stocks to pick

    Return:
        - A tuple -> (total profit, list of picked stocks)
    """
    if stocks:
        # recursively call bruteforce and start to evaluate possibilities from the last item in stocks
        # 1st possibility: skip the stock
        x, combi1 = bruteforce(value, stocks[1:], picked)

        pick = stocks[0]
        if pick[1] <= value:
            # second possibility: pick the stock
            # update new value
            y, combi2 = bruteforce(value - pick[1], stocks[1:], picked + [pick])

            # return the combination with the best profit
            if x < y:
                return y, combi2
        return x, combi1
    else:
        return sum(i[2] for i in picked), picked


if __name__ == "__main__":
    if len(sys.argv) > 1:
        stocks = serialize_data_from_csv(sys.argv[1])
        results = bruteforce(500, stocks)
        calculate_profit(results)
