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
        dataset.append((data[0], float(data[1]), float(data[1]) * float(data[2]) / 100))
    return dataset
