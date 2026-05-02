
#Approach 1 (2D Matrix):
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[[1]*n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]=grid[i-1][j]+grid[i][j-1]

        return grid[m-1][n-1]
        

#Approach 2 Optimized (1D Matrix):
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr_row = [1] * n
        prev_row = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                curr_row[j] = curr_row[j - 1] + prev_row[j]    
            curr_row, prev_row = prev_row, curr_row
        
        return prev_row[-1]
    
#Apprach 3 (Mathematical):
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)