class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        res = float("inf")
        prefixRow1, prefixRow2 = grid[0].copy(), grid[1].copy()
        for i in range(1, N):
            prefixRow1[i] +=  prefixRow1[i - 1]
            prefixRow2[i] +=  prefixRow2[i - 1]
        for i in range(N):
            top = prefixRow1[-1] - prefixRow1[i]
            bottom = prefixRow2[i-1] if i > 0 else 0
            secondRobot = max(top, bottom)
            res = min(res, secondRobot)
        return res
        

        