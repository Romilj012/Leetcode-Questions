class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # q = deque()
        # for i in range(1, n+1):
        #     q.append(i)
        # while len(q) > 1:
        #     q.rotate(-(k-1))
        #     q.popleft()
        # return q[0]
        winner = 0  # Base case for n = 1 (0-based index)
        for i in range(2, n + 1):  # Solve for 2 to n people
            winner = (winner + k) % i
        return winner + 1  # Convert to 1-based index


