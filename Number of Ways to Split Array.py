class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        pref[0] = nums[0]
        suff[-1] = nums[-1]

        for i in range(1, n):
            pref[i] = nums[i] + pref[i - 1]
        
        for i in range(n-2, -1, -1):
            suff[i] = nums[i] + suff[i + 1]

        cnt = 0
        for i in range(n-1):
            if pref[i] >= suff[i + 1]:
                cnt += 1
        
        return cnt
