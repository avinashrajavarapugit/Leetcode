class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort similar to 2 sum
        but here one pointer will be iterating
        other 2 will be two pointers
        for i
        take l, r 
        l = i + 1 r = n - 1
        tc : o(n) * o(n) + o(nlogn)
        sc : o(1)
        '''
        res = []
        nums.sort()

        for i in range(len(nums)):
            # remplove duplicate cal
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # remplove duplicate cal
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res
