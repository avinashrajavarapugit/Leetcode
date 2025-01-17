class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        x = 0
        for d in derived:
            x ^= d
        return x == 0 
