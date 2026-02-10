# Identifying Compromised Employee Accounts

## Problem Statement

Amazon manages multiple digital storage units that can be accessed and modified by different employees. Unfortunately, a cybercriminal has breached the accounts of some employees, potentially tampering with the storage units accessible by those accounts.

There are:
- `n` employees, identified by IDs from `1` to `n`
- `m` storage units, identified by IDs from `1` to `m`

It is known that **exactly `k` storage units have been tampered with**.

Your task is to determine **which employee accounts have certainly been compromised**.

---

## Input Description

You are given:

- `modifiedUnits`: an array of `k` **distinct integers** representing the IDs of the tampered storage units
- `accessRights`: an array of `n` binary strings, each of length `m`
  - The `j`-th bit of the `i`-th string is `'1'` if employee `i` has access to storage unit `j`

---

## Compromise Rules

An employee is:

### ❌ NOT compromised if:
- They have access to **at least one storage unit that has not been tampered with**

### ✅ Considered compromised **if and only if**:
1. **All** storage units they can access have been tampered with  
2. There exists **at least one storage unit** that:
   - Is accessible by this employee
   - Is **not accessible by any other employee**

---

## Output

Return a **sorted list of employee IDs** that are **certainly compromised**.

- If no employee can be definitively identified as compromised, return `[-1]`

---

## Example

### Input

- k = 3
- modifiedUnits = [1, 2, 4]
- n = 5
- m = 4

- accessRights = [
"1100",
"1110",
"1010",
"0001",
"0001"]


### Access Rights Table

| Employee ID | Accessible Storage Units |
|------------|--------------------------|
| 1 | [1, 2] |
| 2 | [1, 2, 3] |
| 3 | [1, 3] |
| 4 | [4] |
| 5 | [4] |

### Explanation

- Employee **2** is not compromised because storage unit `3` was **not** tampered with
- Employee **3** is not compromised for the same reason
- Employee **1**:
  - Can access only storage units `1` and `2`
  - Both were tampered with
  - Storage units `1` and `2` are also accessed by employees who are known to be uncompromised  
  → Employee **1 is certainly compromised**
- Employees **4 and 5**:
  - Both can access only storage unit `4`
  - But we cannot determine which one was compromised  
  → Neither is conclusively compromised

### Output

[1]


---

## Function Description

Complete the function `findBreachedEmployees`.

### Parameters
- `int modifiedUnits[k]`: IDs of modified storage units
- `string accessRights[n]`: binary strings representing access permissions

### Returns
- `int[]`: sorted list of employee IDs that have been conclusively compromised

---

## Constraints

- `1 ≤ n, m ≤ 2500`
- `1 ≤ k ≤ m`
- `1 ≤ modifiedUnits[i] ≤ m`
- All values in `modifiedUnits` are distinct
- Each string in `accessRights` contains only `'0'` or `'1'`
