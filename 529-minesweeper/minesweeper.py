class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def numOfAdjacentMines(board, row, col):
            numAdjacentMines = 0
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if r >= 0  and r < len(board) and c >=0 and c <len(board[row]) and board[r][c]=='M':
                        numAdjacentMines+=1  
            return numAdjacentMines

        if not board:
            return board
        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            numOfMines = numOfAdjacentMines(board, row, col)
            if numOfMines:
                board[row][col] = str(numOfMines)
            else:
                board[row][col] = 'B'
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        if r >= 0  and r < len(board) and c >=0 and c <len(board[r]) and board[r][c]!='B':
                            self.updateBoard(board, [r,c])
        return board
