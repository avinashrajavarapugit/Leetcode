import math
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        '''
        iterate from back if ele is seen stop there return index / 3
        '''
        seen = set()
        last = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                last = i + 1
                break
            seen.add(nums[i])

        return math.ceil(last/3)
            
