class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()
        for i in range(1, n+1):
            q.append(i)
        while len(q) > 1:
            q.rotate(-(k-1))
            q.popleft()
        return q[0]


