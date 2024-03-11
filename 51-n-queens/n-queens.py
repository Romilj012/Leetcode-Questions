class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        solution = [["."] * n for i in range(n)]
        columns = set()
        positiveDiagonal = set() #(r+c)
        negativeDiagonal = set() # (r-c)
        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in solution]
                result.append(copy)
                return
            for c in range(n):
                if c in columns or (r + c) in positiveDiagonal or (r - c) in negativeDiagonal:
                    continue   
                columns.add(c)
                positiveDiagonal.add(r + c)
                negativeDiagonal.add(r - c)
                solution[r][c] = "Q"
                backtracking(r + 1)
                
                columns.remove(c)
                positiveDiagonal.remove(r + c)
                negativeDiagonal.remove(r - c)
                solution[r][c] = "."
        
        backtracking(0)
        return result

         