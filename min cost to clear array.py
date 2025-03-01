import gc
class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)

        gc.collect()
        
        @cache
        def go(i, c):
            left = n - i + int(c != inf)
            if left < 3:
                if c == inf:
                    return max(nums[i:], default=0)
                else:
                    return max(c, max(nums[i:], default=0))
            
            a, b = nums[i: i+ 2]
            drop = 2
            if c == inf:
                c = nums[i + 2]
                drop = 3
            return min(
                go(i + drop, a) + max(b, c),
                go(i + drop, b) + max(a, c),
                go(i + drop, c) + max(a, b)
            )

        go.cache_clear()
        return go(0, inf)
