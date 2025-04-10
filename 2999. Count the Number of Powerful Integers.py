class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        '''
        START, FINISH, LIMIT
        S
        x -> powerful if s suffix of x
        '''
        def solve(i):
            ch = str(i)
            n = len(ch) - len(s)
            if n < 0:
                return 0
            dp = [[0] * 2 for _ in range(n + 1)]
            dp[n][0] = 1
            dp[n][1] = int(ch[n:] >= s)
            for i in range(n - 1, -1, -1):
                digit = int(ch[i])
                dp[i][0] = (limit + 1) * dp[i + 1][0]
                if digit <= limit:
                    dp[i][1] = digit * dp[i + 1][0] + dp[i + 1][1]
                else:
                    dp[i][1] = (limit + 1) * dp[i + 1][0]
            return dp[0][1]
        return solve(finish) - solve(start - 1)
