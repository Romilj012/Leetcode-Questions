class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            if (r,c) in visit or grid[r][c] == 1: 
                return True
            visit.add((r,c)) 
            top = dfs(r - 1, c)
            bottom = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            return top and bottom and left and right
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r,c) not in visit:
                    if dfs(r, c):
                        res += 1
        return res
        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        
        # def dfs(r, c):
        #     # If out of bounds, it touches the boundary
        #     if r < 0 or c < 0 or r >= rows or c >= cols:
        #         return False
            
        #     # If already visited or water, stop
        #     if (r, c) in visited or grid[r][c] == 1:
        #         return True
            
        #     # Mark cell as visited
        #     visited.add((r, c))
            
            # Check all directions and see if any part touches the boundary
            # top = dfs(r - 1, c)
            # bottom = dfs(r + 1, c)
            # left = dfs(r, c - 1)
            # right = dfs(r, c + 1)
            # return top and bottom and left and right
        
        # closed_islands = 0
        
        # # Iterate through the grid
        # for r in range(rows):
        #     for c in range(cols):
        #         # If it's land and not visited, perform DFS
        #         if grid[r][c] == 0 and (r, c) not in visited:
        #             # If DFS confirms it's a closed island, increment count
        #             if dfs(r, c):
        #                 closed_islands += 1
        
        # return closed_islands
            

