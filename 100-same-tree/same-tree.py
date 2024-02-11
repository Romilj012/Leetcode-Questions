# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # Check if both nodes are None
            if not p and not q:
                return True
            # Check if only one of them is None
            if not p or not q:
                return False
                
            if p.val == q.val:
                return dfs(p.right, q.right) and dfs(p.left, q.left)
            else:
                return False

        return dfs(p, q)