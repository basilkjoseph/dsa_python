
from typing import List

#Solution1: Brute Force
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        """
        Find the side length of the largest magic square in the grid.
        A magic square has all rows, columns, and diagonals summing to the same value.
        """
        m = len(grid)  # Number of rows in grid
        n = len(grid[0])  # Number of columns in grid
        k = min(m, n)  # Start with the maximum possible side length
        
        # Try each size from largest to smallest
        while (k != 1):
            # Check all possible positions for a k×k square
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    # Store all sums (rows, cols, diagonals) for this square
                    sums = set()
                    col = [0] * k  # Sum of each column in the square
                    diag = [0, 0]  # diag[0]: main diagonal, diag[1]: anti-diagonal
                    
                    # Iterate through each cell in the k×k square
                    for x in range(i, i + k):
                        row = 0  # Sum of current row in the square
                        for y in range(j, j + k):
                            row += grid[x][y]
                            col[y - j] += grid[x][y]  # Add to corresponding column sum
                            
                            # Check if cell is on main diagonal (top-left to bottom-right)
                            if x - i == y - j:
                                diag[0] += grid[x][y]
                                # For odd-sized squares, count center cell in anti-diagonal too
                                if k % 2 != 0 and x - i == k // 2:
                                    diag[1] += grid[x][y]
                            # Check if cell is on anti-diagonal (top-right to bottom-left)
                            elif x - i + y - j == k - 1:
                                diag[1] += grid[x][y]
                        
                        # Add row sum to the set of all sums
                        sums.add(row)
                    
                    # Add all column sums to the set
                    for val in col:
                        sums.add(val)
                    
                    # Add diagonal sums to the set
                    sums.add(diag[0])
                    sums.add(diag[1])
                    
                    # If all sums are equal (only 1 unique value), it's a magic square
                    if len(sums) == 1:
                        return k
            k -= 1  # Try next smaller size
        
        return 1  # Minimum magic square size is always 1        
