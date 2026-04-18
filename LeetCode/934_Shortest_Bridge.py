from collections import deque
from typing import List

#Approach 1 (Own)
class Solution:
    def connectIslands(self,grid,idx,island):
        directions=((0,1),(0,-1),(1,0),(-1,0))
        bfs=deque()
        bfs.append((idx,1))
        island.add(idx)

        while(bfs):
            (x,y),count=bfs.popleft()
            for dx,dy in directions:
                new_x,new_y=x+dx,y+dy
                if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) and (new_x,new_y) not in island:
                    if grid[new_x][new_y]==1:
                        island.add((new_x,new_y))
                        bfs.append(((new_x,new_y),count+1))

    def bridgeIslands(self,grid,idx,island):
        directions=((0,1),(0,-1),(1,0),(-1,0))
        bfs=deque()
        bfs.append((idx,0))
        visited=set()

        while(bfs):
            (x,y),count=bfs.popleft()
            for dx,dy in directions:
                new_x,new_y=x+dx,y+dy
                if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) and (new_x,new_y) not in visited:
                    if (new_x,new_y) in island:
                        return count
                    if grid[new_x][new_y]==0:
                        visited.add((new_x,new_y))
                        bfs.append(((new_x,new_y),count+1))
        return 101

    def shortestBridge(self, grid: List[List[int]]) -> int:

        islandA=set()
        flag=False
        #Connecting islandA
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.connectIslands(grid,(i,j),islandA)
                    flag=True
                    break
            if flag:
                break

        islandB=set()
        flag=False
        #Connecting islandB
        for i in range(len(grid)):
            for j in range(len(grid[0])):   
                if grid[i][j]==1 and (i,j) not in islandA:
                    self.connectIslands(grid,(i,j),islandB)
                    flag=True
                    break
            if flag:
                break

        min_bridge=101
        if len(islandA)>len(islandB):
            for x,y in islandB:
                min_bridge=min(self.bridgeIslands(grid,(x,y),islandA),min_bridge)
        else:
            for x,y in islandA:
                min_bridge=min(self.bridgeIslands(grid,(x,y),islandB),min_bridge)
        return min_bridge

            
#Approach 2 (Optimized)
class Solution:
    def connectIslands(self,grid,idx,island):
        directions=((0,1),(0,-1),(1,0),(-1,0))
        bfs=deque()
        bfs.append(idx)
        island.add(idx)
        while(bfs):
            (x,y)=bfs.popleft()
            for dx,dy in directions:
                new_x,new_y=x+dx,y+dy
                if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) and (new_x,new_y) not in island:
                    if grid[new_x][new_y]==1:
                        island.add((new_x,new_y))
                        bfs.append((new_x,new_y))

    def bridgeIslands(self,grid,island):
        directions=((0,1),(0,-1),(1,0),(-1,0))
        bfs=deque((cell,0) for cell in island)
        visited=set(island)
        while(bfs):
            (x,y),count=bfs.popleft()
            for dx,dy in directions:
                new_x,new_y=x+dx,y+dy
                if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) and (new_x,new_y) not in visited:
                    if grid[new_x][new_y]==1:
                        return count
                    visited.add((new_x,new_y))
                    bfs.append(((new_x,new_y),count+1))
        return -1

    def shortestBridge(self, grid: List[List[int]]) -> int:
        island=set()
        flag=False
        #Connecting island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.connectIslands(grid,(i,j),island)
                    flag=True
                    break
            if flag:
                break
        return self.bridgeIslands(grid,island)
        