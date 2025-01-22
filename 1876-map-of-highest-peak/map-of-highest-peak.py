class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        res = [[-1]* cols for _ in range(rows)]
        visited = set()
        que = deque()
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    res[r][c] = 0
                    que.append((r,c))
                    visited.add((r,c))
        directions = [[0,1],[-1,0],[1,0],[0,-1]]
        while que:
            for i in range(len(que)):
                r, c = que.popleft()
                for dr, dc in directions:
                    ro, co = dr + r , dc + c
                    if ro < 0 or co <0 or ro == rows or co == cols or (ro,co) in visited:
                        continue
                    res[ro][co]= res[r][c] + 1
                    que.append((ro,co))
                    visited.add((ro,co))
        return res