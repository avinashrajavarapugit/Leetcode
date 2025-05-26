class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        n 2 i, j check eversubarraycnt

        use sliding window and shrink nlogn

        use hashmap if there is prefsum - k in map add to cnt
        '''
        count = 0
        prefix_sum = 0
        hashmap = {0: 1}

        for num in nums:
            prefix_sum += num
            count += hashmap.get(prefix_sum - k, 0)
            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

        return count
