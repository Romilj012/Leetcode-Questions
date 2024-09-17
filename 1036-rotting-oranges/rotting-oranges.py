class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute, freshOrange = 0, 0
        row, col = len(grid), len(grid[0])
        que = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    freshOrange +=1
                if grid[r][c] == 2:
                    que.append([r,c])
        directions = [[0,1],[-1,0],[1,0],[0,-1]]
        while que and freshOrange > 0:
            for i in range(len(que)):
                r, c = que.popleft()
                for dr, dc in directions:
                    ro, co = dr + r , dc + c
                    if ro < 0 or co <0 or ro == row or co == col or grid[ro][co] != 1:
                        continue
                    grid[ro][co]= 2
                    que.append([ro,co])
                    freshOrange -=1
            minute +=1
        return minute if freshOrange == 0 else -1