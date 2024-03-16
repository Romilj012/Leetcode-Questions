class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visitSet = set()
        area = 0
        def dfs(i, j):
            if i<0 or j<0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0 or (i, j) in visitSet:
                return 0
            visitSet.add((i,j))
            return (1 + dfs(i-1, j) + 
            dfs(i+1, j) + 
            dfs(i, j-1) + 
            dfs(i, j+1))
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                    area = max(area, dfs(r, c))
        return area

                        
            
        