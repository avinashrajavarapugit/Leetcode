class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)
        
        count = 0
        for c in string.ascii_lowercase:
            if c in pos:
                s, e = pos[c][0], pos[c][-1]
                if e - s + 1 >= 3:
                    count += sum(any(s < x < e for x in v) for v in pos.values())

        return count
