class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0
        def dfs(i, j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            res = grid[i][j]
            grid[i][j] = 0
            for u, v in d:
                res += dfs(i + u, j + v, grid)
            
            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    ans = max(ans, dfs(i, j, grid))
                
        return ans
