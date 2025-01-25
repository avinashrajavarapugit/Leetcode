class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums = sorted(map(tuple, map(reversed, enumerate(nums))))
        res = []
        for x in nums:
            if not res or abs(res[-1][-1][0]-x[0]) > limit:
                res.append([])
            res[-1].append(x)
        ans = [-1]*len(nums)
        for g in res:
            pos = sorted(x[1] for x in g)
            for (p, (v, _)) in zip(pos, g):
                ans[p] = v
        return ans
