from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # Initialize starting position from first point
        x_i = points[0][0]
        y_i = points[0][1]
        
        # Track cumulative minimum time
        min_time = 0
        
        # Iterate through each subsequent point
        for i in range(1, len(points)):
            # Get current point coordinates
            x = points[i][0]
            y = points[i][1]
            
            # Calculate distance using Chebyshev distance (max of absolute differences)
            # Can move diagonally, so time is the maximum of horizontal/vertical distance
            min_time += max(abs(x - x_i), abs(y - y_i))
            
            # Update current position for next iteration
            y_i = y
            x_i = x
        
        return min_time
        
