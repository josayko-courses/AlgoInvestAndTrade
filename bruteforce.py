"""Bruteforce algorithm.

"""
import sys


def serialize_data_from_csv(filepath):
    """Serialize data as -> dataset = [(name, price, profit)].
    Profit is the profit ratio value of the price -> float(data[1]) * float(data[2]) / 100)
    """
    with open(filepath, "r") as file:
        # Split lines into an array
        lines = file.read().splitlines()
        lines.pop(0)

    dataset = []
    for line in lines:
        data = line.split(',')
        dataset.append((data[0], float(data[1]), float(data[1]) * float(data[2]) / 100))
    return dataset


def calculate_profit(results):
    desc = ["Name", "Price $", "Profit $"]
    print(f"{desc[0]:{' '}^{10}} {desc[1]:{' '}^{10}} {desc[2]:{' '}^{10}}")
    for stock in results[1]:
        print(f"{stock[0]:{' '}<{10}} {stock[1]:{' '}^{10}} {stock[2]:{' '}^{10}}")
    valuation = sum(i[1] for i in results[1])
    print("Portfolio value:", valuation)
    print("Cumulative profits:", "{:.2f}".format(results[0]))
    print("Total return:", "{:.2f}".format(valuation + results[0]))


def bruteforce(value, stocks, picked=[]):
    """Try all possible combinations recursively to get the best profit return.

    Args:
        - value: maximum possible value of a combination
        - stocks: a list of tuples representing the stocks -> stocks = [(name, price, profit)]
        - picked: a list of the stocks to pick

    Return:
        - A tuple -> (total profit, list of picked stocks)
    """
    if stocks:
        # recursively call bruteforce by removing the first stock each time
        x, combi1 = bruteforce(value, stocks[1:], picked)

        # pick the first stock if its price is less or equals to value
        pick = stocks[0]
        if pick[1] <= value:

            #  add picked stock, update new value and recursively call bruteforce by removing it
            y, combi2 = bruteforce(value - pick[1], stocks[1:], picked + [pick])

            # return the combination with the best profit
            if x < y:
                return y, combi2
        return x, combi1
    else:
        return sum(i[2] for i in picked), picked


if __name__ == "__main__":
    stocks = serialize_data_from_csv(sys.argv[1])
    results = bruteforce(500, stocks)
    calculate_profit(results)
