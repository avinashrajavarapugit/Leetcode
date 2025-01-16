class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        def xs(a):
            x = 0
            for i in a:
                x ^= i
            return x
        res = 0
        if len(nums2) % 2 != 0:
            res ^= xs(nums1)
        if len(nums1) % 2 != 0:
            res ^= xs(nums2)
        
        return res
