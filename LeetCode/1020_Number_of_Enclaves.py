from typing import List
from collections import deque

# Approach: 1

class Solution:
    def dfs(self,grid,visited,pos,directions):
        flag=False
        if pos[0]==0 or pos[0]==len(grid)-1 or pos[1]==0 or pos[1]==len(grid[0])-1:
            flag=True
        visited.add((pos[0],pos[1]))
        count=0
        for dx,dy in directions:
            x=pos[0]+dx
            y=pos[1]+dy
            if 0<=x<len(grid) and 0<=y<len(grid[0]):
                if grid[x][y]==1 and (x,y) not in visited:
                    res=self.dfs(grid,visited,(x,y),directions)
                    count+=res[0]
                    flag=flag|res[1]
        return (count+1,flag)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited=set()
        directions=((0,1),(0,-1),(1,0),(-1,0))
        result=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    res=self.dfs(grid,visited,(i,j),directions)
                    if res[1]==False:
                        result+=res[0]

        return result
    


# Approach: 2 (optimized)

def numEnclaves(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    directions = ((0,1),(0,-1),(1,0),(-1,0))

    # BFS from every boundary land cell
    bfs = deque()
    for r in range(rows):
        for c in range(cols):
            if (r == 0 or r == rows-1 or c == 0 or c == cols-1) and grid[r][c] == 1:
                bfs.append((r, c))
                visited.add((r, c))

    # Flood fill — mark all land connected to boundary
    while bfs:
        r, c = bfs.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1 and (nr,nc) not in visited:
                visited.add((nr, nc))
                bfs.append((nr, nc))

    # Count unvisited land cells — these are enclaves
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                count += 1
    return count