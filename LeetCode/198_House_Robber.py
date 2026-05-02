from typing import List

#Approach 1: (Recursion with memoization)
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[-1]*len(nums)
        def dfs(i):
            if i>=len(nums):
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i]= max(dfs(i+1),nums[i]+dfs(i+2))
            return memo[i]
        
        return dfs(0)

#Approach 2: (Bottom up)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        money=[0]*n
        if n==1:
            return nums[0]
        
        money[0]=nums[0]
        money[1]=max(nums[0],nums[1])

        for i in range(2,n):
            rob=nums[i]+money[i-2]
            skip=money[i-1]
            money[i]=max(rob,skip)

        return money[-1]
        
#Approach 3: (Space Optimized)
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_rob = max_rob = 0

        for cur_val in nums:
            temp = max(max_rob, prev_rob + cur_val)
            prev_rob = max_rob
            max_rob = temp
        
        return max_rob