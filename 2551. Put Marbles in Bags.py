class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        '''
        minscore - ensure max ele is min middle of i, j
        maxscore - ensure max ele is either i, j. Use this greedy op
        sort the adj weight array
        take k ele is low
        rem high
        res -> high - low
        '''
        n = len(weights)
        if k == 1:
            return 0
        costs = []
        for i in range(1, n):
            costs.append(weights[i - 1] + weights[i])
        costs.sort()
        m = k - 1
        low = sum(costs[:m])
        high = sum(costs[-m:])
        return high - low
