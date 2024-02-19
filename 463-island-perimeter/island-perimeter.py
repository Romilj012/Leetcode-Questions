# DFS solution
# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         visitSet = set()
#         def dfs(i,j):
#             if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == 0:
#                 return 1
#             if (i,j) in visitSet:
#                 return 0

#             visitSet.add((i,j))
#             perimeter = dfs(i,j+1)
#             perimeter += dfs(i+1, j)
#             perimeter += dfs(i, j-1)
#             perimeter += dfs(i-1, j)
#             return perimeter
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]:
#                     return dfs(i,j)

# Array solution
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4  # Assume 4 sides for each land cell

                    # Check left neighbor
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2  # Subtract 2 for shared left edge

                    # Check top neighbor
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2  # Subtract 2 for shared top edge

        return perimeter
        