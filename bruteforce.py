"""Bruteforce algorithm.

"""
import sys


def serialize_data_from_csv(filepath):
    with open(filepath, "r") as file:
        # Split lines into an array
        lines = file.read().splitlines()
        lines.pop(0)

    dataset = []
    for line in lines:
        data = line.split(',')
        dataset.append((data[0], float(data[1]), float(data[2])))
    return dataset


def calculate_profit(results):
    portfolio = results[1]
    total = 0
    for stock in portfolio:
        profit = stock[1] * stock[2] / 100
        print(f"{stock[0]:{' '}<{10}} {stock[1]:{' '}<{10}} {stock[2]}% {profit:{' '}^{10}}")
        total += profit
    print("Portfolio value:", sum(i[1] for i in portfolio))
    print("Total profit:", "{:.2f}".format(total))


def bruteforce(value, stocks, picked=[]):
    """Try all possible combinations to get the best profit return."""
    if stocks:
        x, lst_x = bruteforce(value, stocks[1:], picked)
        # pick first stock anc compare its price with value
        pick = stocks[0]
        if pick[1] <= value:
            y, lst_y = bruteforce(value - pick[1], stocks[1:], picked + [pick])
            if x < y:
                return y, lst_y
        return x, lst_x
    else:
        return sum(i[2] for i in picked), picked


if __name__ == "__main__":
    stocks = serialize_data_from_csv(sys.argv[1])
    results = bruteforce(500, stocks)
    calculate_profit(results)
