class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        perform sliding window
        go r increment l
        '''
        d={}
        sum=0
        count=0
        for i in range(len(nums)):
            if sum in d:
                d[sum]+=1
            else:
                d[sum]=1
            sum+=nums[i]
            if sum-k in d:
                count+=d[sum-k]
        return count
