class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr, n):
            steps = 0
            first, last = curr, curr
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps
        
        curr = 1
        k -= 1  # because we start from the first number
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1  # move to the next sibling
            else:
                curr *= 10  # move to the next child
                k -= 1  # for the root node (curr itself)
        
        return curr



 