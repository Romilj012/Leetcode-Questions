class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        fibonacci = [0]* (n+1)
        fibonacci[0] = 0
        fibonacci[1] = 1
        for i in range(2, n+1):
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
        return fibonacci[n]

            
        