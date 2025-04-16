class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        '''
        i, j  i < j nums[i] = nums[j]
        kpairs of (i, j)
        1 1 1 1
        01 02 12 03 13 23
        ((n - 1)*(n))//2

        sliding window and dict? -- possible
        '''
        from collections import defaultdict
        d = defaultdict(int)  
        l = 0  
        cnt = 0  
        res = 0  
        for r in range(len(nums)):
            cnt += d[nums[r]]  
            d[nums[r]] += 1  
            while cnt >= k:
                res += len(nums) - r  
                cnt -= d[nums[l]] - 1 
                d[nums[l]] -= 1  
                l += 1 

        return res
