class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for x in s:
            if x - 1 not in s:
                cnt = 0
                curr = x
                while curr in s:
                    cnt += 1
                    curr += 1
                res = max(res, cnt)
        return res
