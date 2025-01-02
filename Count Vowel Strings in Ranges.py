class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pf = []
        curr = 0
        for w in words:
            curr += w[0] in 'aeiou' and w[-1] in 'aeiou'
            pf.append(curr)
        
        res = []
        for l, r in queries:
            amount = pf[r] - (pf[l - 1] if l else 0)
            res.append(amount)
        return res
