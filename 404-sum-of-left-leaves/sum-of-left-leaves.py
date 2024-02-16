# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.calc = 0
        def dfs(root, isLeft):
            if not root:
                return 0
            if not root.left and not root.right and isLeft:
                self.calc += root.val
            dfs(root.left, True)
            dfs(root.right, False)
        dfs(root, False)
        return self.calc