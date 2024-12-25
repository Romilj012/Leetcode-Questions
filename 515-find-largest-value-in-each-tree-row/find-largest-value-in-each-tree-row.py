# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return []
        queue = deque([root])
        while queue:
            maxValue = float('-inf')
            for i in range(len(queue)):
                current = queue.popleft()
                maxValue = max(maxValue, current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            res.append(maxValue)
        return res