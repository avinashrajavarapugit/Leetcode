class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        c = 0
        f = False
        fr = -1
        sc = -1
        c = 0
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c += 1
                if c > 2:
                    return False
                if not f:
                    f = True
                    fr = i
                else:
                    sc = i
        
        if fr == -1 or sc == -1:
            return False
        return s1[sc] == s2[fr] and s1[fr] == s2[sc]
        
