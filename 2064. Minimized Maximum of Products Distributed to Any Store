class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def is_possible(k):
            return sum(ceil(q / k) for q in quantities) <= n

        return bisect_left(range(1, max(quantities) + 1), True, key=is_possible) + 1
