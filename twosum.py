class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        z = []
        for i in range(n-1):
            for j in range(i+1,n):
                if(nums[i]+nums[j]==target):
                    print([i,j])
                    z.append(i)
                    z.append(j)
        return z
