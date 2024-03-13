class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        noOfIslands = 0
        def bfs(r, c):
            que = collections.deque()
            visited.add((r,c))
            que.append((r,c))
            while que:
                row, col = que.popleft()
                directions =[[1,0], [-1,0], [0,-1],[0,1]]
                for drow, dcol in directions:
                    r, c = row + drow, col + dcol
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited:
                        que.append((r,c))
                        visited.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r,c)
                    noOfIslands +=1 
        return noOfIslands
        