class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        maintain count array if any cnt becomes 2 consider lenght not change

        ex abc - 3
        abca - cnt becomes 2 at a incrmenet left pointer ny 1 res - 3
        bbbbb
        pwwkew - pw - 2
        w
        0(n) + o(n) --> o(2n)
        o(26)
        '''
       
        l = 0
        n = len(s)
        res = 0
        cnt = collections.defaultdict(int)
        for i in range(n):
            if cnt[ord(s[i])] == 1:
                cnt[ord(s[i])] -= 1
                while s[l] != s[i]:
                    cnt[ord(s[l])] -= 1
                    l += 1
                l += 1
            cnt[ord(s[i])] += 1
            res = max(res, i - l + 1)
        return res
                
