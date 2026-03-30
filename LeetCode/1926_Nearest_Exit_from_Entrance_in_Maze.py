from collections import deque
from typing import List

#Approach: 1

class Solution:
#Checking for valid cell
    def isValidCell(self,maze,pos):
        if pos[0]<0 or pos[0]>=len(maze) or pos[1]<0 or pos[1]>=len(maze[0]) or maze[pos[0]][pos[1]]=='+' :
            return False
        else:
            return True
#Checking for exit
    def isExit(self,maze,pos,entrance):
        if (((pos[0]==len(maze)-1 or pos[0]==0) and maze[pos[0]][pos[1]]=='.') or ((pos[1]==len(maze[0])-1 or pos[1]==0) and maze[pos[0]][pos[1]]=='.')) and pos!=entrance:
            return True
        else:
            return False

#Main function
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions=[[0,-1],[0,1],[-1,0],[1,0]]
        bfs=deque()
        steps=0
        visited=[[0]*len(maze[0]) for _ in range(len(maze))]
        dummy=[-1,-1]
        visited[entrance[0]][entrance[1]]=1
        bfs.append(entrance)
        bfs.append(dummy)

        while bfs:
            cur_pos=bfs.popleft()
            if cur_pos==dummy:
                if not bfs:
                    return -1
                steps+=1
                bfs.append(dummy)
                continue
            if self.isExit(maze,cur_pos,entrance):
                return steps
            for dir in directions:
                new_pos=[x+y for x,y in zip(cur_pos,dir)]
                if self.isValidCell(maze,new_pos) and visited[new_pos[0]][new_pos[1]]==0:
                    visited[new_pos[0]][new_pos[1]]=1
                    bfs.append(new_pos)

        return -1


#Approach: 2 (optimized)

def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
    rows, cols = len(maze), len(maze[0])
    directions = [(0,-1),(0,1),(-1,0),(1,0)]
    
    start = (entrance[0], entrance[1])
    visited = {start}
    bfs = deque([(start, 0)])  # carry steps in the tuple — no dummy node needed

    while bfs:
        (r, c), steps = bfs.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.' and (nr, nc) not in visited:
                # Check exit inline
                if nr == 0 or nr == rows-1 or nc == 0 or nc == cols-1:
                    return steps + 1
                visited.add((nr, nc))
                bfs.append(((nr, nc), steps + 1))

    return -1