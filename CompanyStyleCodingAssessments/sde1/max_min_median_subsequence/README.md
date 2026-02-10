# Maximum and Minimum Median of Subsequences

## Problem Statement

A new Amazon intern encountered a challenging task.

The intern is given an array of `n` integers, where the value of the `i`-th element is represented by `values[i]`.

Given:
- An integer array `values`
- An integer `k`

The task is to find the **maximum** and **minimum median** among **all subsequences of length `k`**.


---
## Example

### Input

- n = 3
- values = [1, 2, 3]
- k = 2


### Subsequences of Length `k`

| Subsequence | Median |
|------------|--------|
| [1, 2]     | 1      |
| [1, 3]     | 1      |
| [2, 3]     | 2      |

### Output

[2, 1]


- **Maximum median** = `2`
- **Minimum median** = `1`

---

## Function Description

Complete the function `medians`.

### Parameters
- `int values[n]`: array of integers
- `int k`: length of the subsequence

### Returns
- `int[2]`:  
  `[maximum_median, minimum_median]`

---

## Constraints

- `1 ≤ n ≤ 10^5`
- `0 ≤ values[i] ≤ 10^9`
- `1 ≤ k ≤ n`

---

