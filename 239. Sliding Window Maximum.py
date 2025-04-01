class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        '''
        l to r

        1 3 -1 -3 5 3 6 7
        3 3 5 5 6 7

        sliding window if k size is there 
        use motonic stack concept

        for better add and del operations use deque
        o(n) + o(n)
        o(k) --> dq + o(n - k) --> res
        '''
        n = len(arr)
        dq = collections.deque()
        res = []

        for i in range(n):
            if dq and dq[0] <= i - k:
                dq.popleft()
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            if (i >= k - 1):
                res.append(arr[dq[0]])
        return res
