# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # q = deque([root])
        # level = 0
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        s = [[root, 1]]
        res = 1
        while s:
            node, depth = s.pop()
            if node:
                res = max(res, depth)
                s.append([node.left, depth + 1])
                s.append([node.right, depth + 1])
        return res


        