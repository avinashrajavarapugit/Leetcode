class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            x_par = find(x)
            y_par = find(y)
            if x_par == y_par: return False
            
            parents[x_par] = y_par 
            return True
        
        for x, y in edges:
            if not union(x, y):
                return [x, y]
