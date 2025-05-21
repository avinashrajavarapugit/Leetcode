class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        ans = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    ans.add((r, c))
        
        for r, c in ans:
            matrix[r] = [0] * cols
            for row in matrix:
                row[c] = 0
