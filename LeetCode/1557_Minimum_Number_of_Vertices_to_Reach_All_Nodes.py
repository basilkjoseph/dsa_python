from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        hash=[-1]*n
        result=[]
        for srce,tgt in edges:
            hash[tgt]=1
        for i,node in enumerate(hash):
            if node==-1:
                result.append(i)  
                   
        return result