from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])

        self.a = [[0] * (m + 1) for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.a[i][j] = matrix[i-1][j-1] + self.a[i-1][j] + self.a[i][j-1] - self.a[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        return self.a[r2][c2] - self.a[r1-1][c2] - self.a[r2][c1-1] + self.a[r1-1][c1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
