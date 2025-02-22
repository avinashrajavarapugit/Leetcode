class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res = 0
        s = input.split('\n')
        paths = {}
        for c in s:
            level = 0
            while level < len(c) and c[level] == '\t':
                level += 1

            path_len = len(c) if level == 0 else paths[level - 1] + 1 + len(c[level:])

            if '.' in c:
                res = max(res, path_len)
            else:
                paths[level] = path_len
            
        return res
