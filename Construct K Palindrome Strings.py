class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k == len(s):
            return True
        if k > len(s):
            return False
        c = Counter(s)
        cnt = 0
        for u, v in c.items():
            if v % 2 != 0:
                cnt += 1
            
            if cnt > k:
                return False
        
        return True
