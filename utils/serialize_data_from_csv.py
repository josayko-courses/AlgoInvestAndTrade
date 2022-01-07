"""Serialize data from CSV files

"""


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
        # Ignore stock data if its price is less or equals to zero
        if float(data[1]) > 0:
            dataset.append((data[0], float(data[1]), float(data[1]) * float(data[2]) / 100))
    dataset = sorted(dataset, key=lambda x: x[1], reverse=True)
    return dataset
