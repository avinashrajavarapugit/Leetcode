class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        sort and take kth ele
        inplce -> tc: o(nlogn) sc: o(1)
        out -> sc:o(n)

        create a max heap
        root will be max ele remove k max ele

        tc -> o(n) sc: o(n)

        no need of consider n ele in heap we just need k max ele
        perfforrm heap opration while iterating
        sc becomes -> o(k)

        quick select:
        - pick an arbitrary pivot element
        - smaller nums go to the left. larger nums go to the right. same elements go to the mid.
        - if len(larger) == k - 1, we know mid is the kth largest
            * double checking the edge case
        '''
        def quick_select(nums, k):
            # search for the kth largest element in nums
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    right.append(num)
                elif num < pivot:
                    left.append(num)
                else:
                    mid.append(num)

            if len(right) >= k:
                return quick_select(right, k)
            
            if len(right) + len(mid) < k:
                return quick_select(left, k - len(right) - len(mid))

            return pivot
        
        return quick_select(nums, k)
