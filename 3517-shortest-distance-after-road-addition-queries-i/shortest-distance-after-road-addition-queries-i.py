class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i+1] for i in range(n)]
        def shortPath():
            q = deque()
            q.append((0,0))
            visit = set()
            visit.add((0,0))
            while q:
                curr, length = q.popleft()
                if curr == n-1:
                    return length
                for nei in adj[curr]:
                    if nei not in visit:
                        q.append((nei, length + 1))
                        visit.add(nei)
        
        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(shortPath())
        return res
        