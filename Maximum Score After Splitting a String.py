class Solution:
    def maxScore(self, s: str) -> int:
        pref = [0] * len(s)
        pref[0] = 1 if s[0] == '0' else 0
        for i in range(1, len(s)):
            if s[i] == '0':
                pref[i] += 1
            pref[i] += pref[i - 1]
        
        suff = [0] * len(s)
        suff[-1] = 1 if s[-1] == '1' else 0
        for i in range(len(s)-2, -1, -1):
            if s[i] == '1':
                suff[i] += 1
            suff[i] += suff[i + 1]
        
        # print(pref)
        # print(suff)
        res = 0
        for i in range(len(s)-1):
            res = max(res, pref[i] + suff[i + 1])
        return res
Maximum Score After Splitting a String
