---
marp: true
theme: gaia
---

# Presentation

---

- Bruteforce algorithm

  - Time complexity is exponential: **O(2^N)**.
    The number of combinations is 2^N which N is the number of stocks.

  - Space complexity is linear: **O(N)**.
    Memory is allocated for each recursion needed to compute a combination.

---

<style>
  .container { display: flex; }
  .col { flex: 1;}
</style>
<div class="container">
  <div class="col">

|     | A   | B   |
| --- | --- | --- |
| 1   | 0   | 0   |
| 2   | 0   | 1   |
| 3   | 1   | 0   |
| 4   | 1   | 1   |

  </div>
  <div class="col">

|     | A   | B   | C   |
| --- | --- | --- | --- |
| 1   | 0   | 0   | 0   |
| 2   | 0   | 0   | 1   |
| 3   | 0   | 1   | 0   |
| 4   | 0   | 1   | 1   |
| 5   | 1   | 0   | 0   |
| 6   | 1   | 0   | 1   |
| 7   | 1   | 1   | 0   |
| 8   | 1   | 1   | 1   |

  </div>
  <div class="col">

| N   | 2^N     |
| --- | ------- |
| 0   | 1       |
| 1   | 2       |
| 2   | 4       |
| 3   | 8       |
| 4   | 16      |
| 18  | 262144  |
| 19  | 524288  |
| 20  | 1048576 |

  </div>
</div>

---

- Bruteforce visual representation

![w:1200](bruteforce_tree.svg)

---

```python
def bruteforce(value, stocks, picked=[]):
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

```

---

- Optimized algorithm

  - Time complexity is: **O(m \* N)**.
    The numbers of subproblems which m represents every possible value (or capacity) and N the number of items.

  - Space complexity is: **O(m \* N)**.
    The size of the matrix containing each subproblems.

Avoid redundant events by breaking them in subproblems so don't need to calculate all the possibilities.
Start from the simpliest to the most complex event.
Each computation is incremental.

---

---

```python
def optimized(value, stocks):
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

    # Retrieve picked stocks from the best solution
    while v >= 0 and n >= 0:
        pick = stocks[n - 1]
        if m[n][trunc(v)] == m[n - 1][trunc(v - pick[1])] + pick[2]:
            picked.append(pick)
            v -= pick[1]
        n -= 1
    return m[-1][-1], picked
```

---

# End
