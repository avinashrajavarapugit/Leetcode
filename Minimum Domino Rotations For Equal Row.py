class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        s = reduce(set.__and__, (set(d) for d in zip(A, B)))
        if not s: return -1
        x = s.pop()
        return min(len(A) - A.count(x), len(B) - B.count(x))
        
