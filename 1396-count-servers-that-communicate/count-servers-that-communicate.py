class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_cnt, col_cnt  = [0]*rows, [0]*cols
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_cnt[r] += 1
                    col_cnt[c] += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (row_cnt[r] > 1 or col_cnt[c] > 1):
                    res+= 1
        return res