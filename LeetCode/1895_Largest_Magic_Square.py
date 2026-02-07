
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



    def largestMagicSquare_optimized(self, grid: List[List[int]]) -> int:
        """Optimized search using prefix sums for row/column sums.

        Uses row and column prefix sums to compute row/column sums in O(1)
        for any sub-row or sub-column. Diagonals are computed directly.
        The function tries square sizes from largest to smallest and returns
        the first (largest) valid magic square size found.
        """
        m = len(grid)
        n = len(grid[0])

        # rowPrefix[i][j] = sum of grid[i][0..j]
        rowPrefix = [[0] * n for _ in range(m)]
        # colPrefix[i][j] = sum of grid[0..i][j]
        colPrefix = [[0] * n for _ in range(m)]

        # Build row prefix sums
        for i in range(m):
            rowPrefix[i][0] = grid[i][0]
            for j in range(1, n):
                rowPrefix[i][j] = rowPrefix[i][j - 1] + grid[i][j]

        # Build column prefix sums
        for j in range(n):
            colPrefix[0][j] = grid[0][j]
            for i in range(1, m):
                colPrefix[i][j] = colPrefix[i - 1][j] + grid[i][j]

        # Try square sizes from largest to smallest
        for size in range(min(m, n), 1, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    # Collect all row sums, column sums and diagonal sums
                    magicSum = set()
                    diagSum = 0
                    antiDiagSum = 0

                    # Add row sums for each row in the square using rowPrefix
                    for x in range(i, i + size):
                        row_sum = rowPrefix[x][j + size - 1] - (0 if j == 0 else rowPrefix[x][j - 1])
                        magicSum.add(row_sum)

                    # Add column sums for each column in the square using colPrefix
                    for y in range(j, j + size):
                        col_sum = colPrefix[i + size - 1][y] - (0 if i == 0 else colPrefix[i - 1][y])
                        magicSum.add(col_sum)

                    # Compute main and anti-diagonal sums directly
                    for d in range(size):
                        diagSum += grid[i + d][j + d]
                        antiDiagSum += grid[i + d][j + size - 1 - d]

                    magicSum.add(diagSum)
                    magicSum.add(antiDiagSum)

                    # If all sums are equal, we found a magic square
                    if len(magicSum) == 1:
                        return size

        return 1
                