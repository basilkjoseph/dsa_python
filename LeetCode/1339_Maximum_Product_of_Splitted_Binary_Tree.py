# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minDiff= float('inf')  # Track minimum difference (unused in final solution)
        self.totalSum=0  # Store the total sum of all node values
        self.maxProd=0  # Track the maximum product found
    def sumTillNode(self,root:Optional[TreeNode]):
        # Base case: if node is None, return 0
        if root is None:
            return 0
        # Recursively calculate sum of left and right subtrees and add root's value
        # Update root.val to be the sum of the entire subtree rooted at this node
        root.val=root.val+self.sumTillNode(root.left)+self.sumTillNode(root.right)
        return root.val

    def bfs(self,root:Optional[TreeNode]):
        # Base case: stop if node is None
        if root is None:
            return
        
        # If left child exists, consider cutting the edge between root and left child
        # leftSum = sum of left subtree, rightSum = total sum - left subtree sum
        # Product = leftSum * rightSum (sum of remaining tree after cut)
        if root.left is not None:
            leftSum=root.left.val
            rightSum=self.totalSum-leftSum
            self.maxProd=max(self.maxProd,leftSum*rightSum)
        
        # If right child exists, consider cutting the edge between root and right child
        # Similar logic: rightSum = sum of right subtree, leftSum = total sum - right subtree sum
        if root.right is not None:
            rightSum=root.right.val
            leftSum=self.totalSum-rightSum
            self.maxProd=max(self.maxProd,leftSum*rightSum)

        # Recursively traverse left and right subtrees to check all possible cuts
        self.bfs(root.left)
        self.bfs(root.right)

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # Step 1: Calculate sum of all nodes in the tree and update each node's value to be its subtree sum
        self.sumTillNode(root)
        # Step 2: Store the total sum for later calculations
        self.totalSum=root.val
        # Step 3: Traverse tree and find the maximum product from all possible edge cuts
        self.bfs(root)
        # Return result modulo 10^9 + 7 as required by problem
        return (self.maxProd%(10**9 + 7))


