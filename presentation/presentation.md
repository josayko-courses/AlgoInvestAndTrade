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

- Optimized algorithm

---

# End
