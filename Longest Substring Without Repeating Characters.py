class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, z, a, b, c = 0, 0, [], [], [], 0
        while j < len(s):
            if s[j] not in s[i:j]:
                z.append(s[i:j+1])
                j += 1
            else:
                i += 1
        a = list(set(z))
        b = list(filter(lambda x: len(set(x)) == len(x), a))
        c = 0 if not b else max(len(s) for s in b)
        return c
