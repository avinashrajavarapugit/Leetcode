class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq = defaultdict(int)
        for w in words2:
            local_freq = Counter(w)
            for i in local_freq:
                freq[i] = max(freq[i], local_freq[i])
        
        ans = []
        for w in words1:
            local_freq = Counter(w)
            add = True

            for i in freq:
                if freq[i] > local_freq[i]:
                    add = False
                    break
            if add:
                ans.append(w)
        return ans
