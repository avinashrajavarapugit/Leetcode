class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        put l = 0
        r = n - 1
        take max area by taking r - l  * min(left height, rightheight)
        if l > r thrn decrement r
        if r > l decrement l
        if euals anything works
        o(n)
        o(1)

        another app:
        maintain max pref and suff arra
        choose min(max[l], max[r]) - height
        o (3n)
        o(2n)
        '''
        n = len(height)
        l = 0
        r = n - 1
        res = 0
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[l] <height[r]:
                l += 1
            else:
                r -= 1
        
        return res
                
