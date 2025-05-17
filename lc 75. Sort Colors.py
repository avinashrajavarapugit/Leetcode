class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        use dutch national flag algorithm
        low poinnts -> 0
        mid -> 1
        high -> 2
        how to buils logic?
        2, 0, 2, 1, 1, 0
        if a[mid] > a[high]-> swap
        l points to 0
        mid points to 0

        """
        n = len(nums)
        l = 0
        m = 0
        r = n - 1
        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 2:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1
            else:
                m += 1
        
