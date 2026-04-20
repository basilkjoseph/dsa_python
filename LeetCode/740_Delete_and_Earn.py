from collections import Counter
from typing import List

#Approach 1 (Brute Force Recursion):
class Solution:
    def deleteAndEarn(self, nums):
        count = Counter(nums)
        unique = sorted(count.keys())
        
        def dfs(i):
            if i >= len(unique):
                return 0
            
            # Option 1: skip current
            skip = dfs(i + 1)
            
            # Option 2: take current
            take = unique[i] * count[unique[i]]
            
            # if next is consecutive, skip it
            if i + 1 < len(unique) and unique[i] + 1 == unique[i + 1]:
                take += dfs(i + 2)
            else:
                take += dfs(i + 1)
            
            return max(skip, take)
        
        return dfs(0)
    

#Approach 2 (Optimization using Memoization):
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count=Counter(nums)
        unique=sorted(count.keys())
        memo=[-1]*len(unique)

        def dfs(i,memo):
            if i>=len(unique):
                return 0

            if memo[i]!=-1:
                return memo[i]

            skip=dfs(i+1,memo)

            take=unique[i] * count[unique[i]]
            
            if i+1<len(unique) and unique[i]+1==unique[i+1]:
                take+=dfs(i+2,memo)
            else:
                take+=dfs(i+1,memo)

            memo[i]=max(skip,take)
            return memo[i]

        return dfs(0,memo)
    

#Approach 3 (Bottom up):

def deleteAndEarn(self, nums: List[int]) -> int:
    count = Counter(nums)
    unique = sorted(count.keys())
    n = len(unique)

    if n == 1:
        return unique[0] * count[unique[0]]

    dp = [0] * n
    dp[0] = unique[0] * count[unique[0]]
    dp[1] = max(dp[0], unique[1] * count[unique[1]]) if unique[1] == unique[0] + 1 \
            else dp[0] + unique[1] * count[unique[1]]

    for i in range(2, n):
        earn = unique[i] * count[unique[i]]
        if unique[i] == unique[i-1] + 1:
            dp[i] = max(dp[i-1], dp[i-2] + earn)
        else:
            dp[i] = dp[i-1] + earn  # no conflict, always take

    return dp[-1]
