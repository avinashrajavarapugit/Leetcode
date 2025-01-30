class Solution:
    def magnificentSets(self, N: int, edges: List[List[int]]) -> int:
        INF = float('inf')
        adj = collections.defaultdict(list)
        for u, v in edges:
            u -= 1
            v -= 1

            adj[u].append(v)
            adj[v].append(u)

        def solve(x):
            d = collections.defaultdict(lambda: INF)
            q = collections.deque()
            d[x] = 1
            q.append(x)

            while q:
                now = q.popleft()

                for v in adj[now]:
                    if d[v] == INF:
                        d[v] = d[now] + 1
                        q.append(v)
                    else:
                        if d[v] % 2 == d[now] % 2:
                            return (-1, -1)
            
            return min(d.keys()), max(d.values())


        best = collections.defaultdict(lambda: 0)
        for i in range(N):
            g, r = solve(i)
            best[g] = max(best[g], r)
            if r == -1:
                return -1
        return sum(best.values())
