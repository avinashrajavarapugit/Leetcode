n = len(days)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + costs[0]
            
            j = i - 1
            while j >= 0 and days[i - 1] - days[j] < 7:
                j -= 1
            dp[i] = min(dp[i], dp[j + 1] + costs[1])
            
            j = i - 1
            while j >= 0 and days[i - 1] - days[j] < 30:
                j -= 1
            dp[i] = min(dp[i], dp[j + 1] + costs[2])
        
        return dp[n]
