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
        dataset.append((data[0], int(data[1]), int(data[2])))
    return dataset


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
    print(results)
