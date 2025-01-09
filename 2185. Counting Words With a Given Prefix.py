class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        m = len(pref)
        for word in words:
            if len(word) < m:
                continue
            if word[:m] == pref:
                cnt += 1
        return cnt
