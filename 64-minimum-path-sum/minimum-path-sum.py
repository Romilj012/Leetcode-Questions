class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if r > 0 and c > 0:
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
                # If we're in the first row, we can only come from the left
                elif r == 0 and c > 0:
                    grid[r][c] += grid[r][c - 1]
                # If we're in the first column, we can only come from above
                elif c == 0 and r > 0:
                    grid[r][c] += grid[r - 1][c]
# The bottom-right cell contains the minimum path sum
        return grid[row - 1][col - 1]


        