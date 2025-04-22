class Solution:
    def trap(self, h: List[int]) -> int:
        '''
        I nned to trap the water
        need to find the min of max height towards left and right
        approach
        find pref max and suff max
        take min(pref, suff) - height[curr]
        tc: o(n) + o(n) + o(n)
        sc: o(n) + o(n)
        2.time is fine I guess. problem with the space?
        yup
        need to perform 2 pointers on it
        take left and right
        move left pointer if left < right
        move right pointer if right > left
        else moving any pointer gives same result
        '''
        l = 0
        r = len(h) - 1
        res = 0
        lmx = h[0]
        rmx = h[-1]
        while l < r:
            if lmx < rmx:
                l += 1
                lmx = max(lmx, h[l])
                res += (lmx - h[l])
            else:
                r -= 1
                rmx = max(rmx, h[r])
                res += (rmx - h[r])
        return res
