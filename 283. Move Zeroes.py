class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        if you find 0
        increment k
        if num > 0 found replca number in [i - k] place
        """
        n = len(nums)
        k = 0
        for i, num in enumerate(nums):
            if num == 0:
                k += 1
            else:
                nums[i - k] = nums[i]
        
        for i in range(n - k, n):
            nums[i] = 0
