class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        d = {}
        print(m,n)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    d[(i,j)] = 0
        for i, j in d:
            # Set the entire row to zero
            for col in range(n):
                matrix[i][col] = 0
            # Set the entire column to zero
            for row in range(m):
                matrix[row][j] = 0


        