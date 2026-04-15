from typing import List

# Disjoint Set Union (DSU) class for union-find operations
class DSU:
    def __init__(self,n):
        # Initialize parent array where each element is its own parent
        self.parent=list(range(n))
        # Initialize rank array to keep track of tree heights for union by rank
        self.rank=[0]*n

    def find(self,x):
        # Path compression: find the root parent and update the parent array
        if self.parent[x]==x:
            return x
        else:
            self.parent[x]=self.find(self.parent[x])
            return self.parent[x]
    
    def union(self,x,y):
        # Find the root parents of x and y
        px=self.find(x)
        py=self.find(y)

        # If they are already in the same set, do nothing
        if px==py:
            return
        
        # Union by rank: attach the smaller tree to the larger one
        if self.rank[px]>self.rank[py]:
            self.parent[py]=px
        elif self.rank[px]<self.rank[py]:
            self.parent[px]=py
        else:
            # If ranks are equal, attach py to px and increase rank
            self.parent[py]=px
            self.rank[py]+=1
        
# Solution class for the Accounts Merge problem
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Initialize DSU with number of accounts
        dsu=DSU(len(accounts))
        # Dictionary to map each email to the first account index it appears in
        all_mails=dict()
        n=len(accounts)
        # Iterate through each account and its emails
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                mail=accounts[i][j]
                # If email not seen before, map it to current account index
                if mail not in all_mails:
                    all_mails[mail]=i
                else:
                    # If email seen before, union the current account with the previous one
                    dsu.union(all_mails[mail],i)
        
        # Dictionary to group emails by their root parent (merged account)
        result_dict=dict()
                
        # Group emails by their root parent
        for mail,idx in all_mails.items():
            idx=dsu.find(idx)
            if idx in result_dict:
                result_dict[idx].append(mail)
            else:
                result_dict[idx]=[mail]
            
        # List to store the final merged accounts
        result=list()
        
        # For each merged group, create the account with name and sorted emails
        for idx,mail in result_dict.items():
            name=accounts[idx][0]
            lst=[name]
            lst.extend(sorted(mail))
            result.append(lst)

        return result

