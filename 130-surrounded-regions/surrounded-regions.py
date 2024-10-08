class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        def captureRegion(r,c):
            if r < 0 or c < 0 or r == row or c == col or board[r][c] != "O":
                return
            board[r][c] = "T"
            captureRegion(r+1,c)
            captureRegion(r-1,c)
            captureRegion(r,c+1)
            captureRegion(r,c-1)

        for r in range(row):
            for c in range(col):
                if (board[r][c] == "O" and (r in [0,row-1] or c in [0,col-1])):
                    captureRegion(r,c)
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(row):
            for c in range(col):
                if board[r][c] == "T":
                    board[r][c] = "O"