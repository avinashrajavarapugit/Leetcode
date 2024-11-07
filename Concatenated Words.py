class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary = set(words)
        r = []
        for word in words:
            n = len(word)
            k = [False] * (n + 1)
            k[0] = True
            
            for i in range(1, n+1):
                for j in range((i == n) and 1 or 0, i):
                    if not k[i]:
                        k[i] = k[j] and word[j:i] in dictionary
            if k[n]:
                r.append(word)
        return r
        
   
