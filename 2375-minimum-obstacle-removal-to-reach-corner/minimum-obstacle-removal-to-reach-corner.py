class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        min_heap = [(0,0,0)] 
        visit = set([(0,0)])
        while min_heap:
            obs, r, c = heapq.heappop(min_heap)
            if (r, c) == (rows-1, cols-1):
                return obs
            nei = [[r+1, c],[r, c+1],[r-1, c],[r, c-1]]
            for nr, nc in nei:
                if (nr,nc) in visit or nr < 0 or nc < 0 or nc == cols or nr == rows:
                    continue
                heapq.heappush(min_heap, (obs + grid[nr][nc], nr, nc))
                visit.add((nr, nc))
            
        