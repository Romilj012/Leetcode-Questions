class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pc, at = set(), set()
        result = []
        def dfs(r, c, oceanSet, prevHeight):
            if r < 0 or c < 0  or r == row or c == col or (r,c) in oceanSet or heights[r][c] < prevHeight:
                return
            oceanSet.add((r,c))
            dfs(r,c-1,oceanSet,heights[r][c])
            dfs(r-1,c,oceanSet,heights[r][c])
            dfs(r+1,c,oceanSet,heights[r][c])
            dfs(r,c+1,oceanSet,heights[r][c])

        for c in range(col):
            dfs(0, c, pc, heights[0][c])
            dfs(row-1, c, at, heights[row-1][c])

        for r in range(row):
            dfs(r, 0, pc, heights[r][0])
            dfs(r, col-1, at, heights[r][col-1])  
        
        for r in range(row):
            for c in range(col):
                if (r,c) in pc and (r,c) in at:
                    result.append([r,c])
        return result