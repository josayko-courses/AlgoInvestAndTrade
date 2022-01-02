"""Calculate profit return of a stocks portfolio

"""


def calculate_profit(results):
    desc = ["Name", "Price $", "Profit $"]
    print(f"{desc[0]:{' '}^{10}} {desc[1]:{' '}^{10}} {desc[2]:{' '}^{10}}")
    for stock in results[1]:
        print(f"{stock[0]:{' '}<{10}} {stock[1]:{' '}^{10}} {stock[2]:{' '}^{10}}")
    valuation = sum(i[1] for i in results[1])
    print("Portfolio value:", valuation)
    print("Cumulative profits:", "{:.2f}".format(results[0]))
    print("Total return:", "{:.2f}".format(valuation + results[0]))
