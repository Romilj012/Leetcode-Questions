class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [[2,1],[-2,1],[1,2],[-1,2],[-1,-2],[1,-2],[2,-1],[-2,-1]]
        visited = defaultdict(list)
        def dp(row, col, moves):
            if (row,col,moves) in visited:
                return visited[(row,col,moves)]
            if row >= n or col >= n or row < 0 or col < 0:
                return 0
            if moves == 0:
                return 1
            res = 0
            for d in directions:
                res += (1/8) * dp(row + d[0], col + d[1], moves - 1)
                visited[(row, col, moves)] = res
            return res
        return dp(row, column, k)
        