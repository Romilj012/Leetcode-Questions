class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            a = str(x)[::-1]
        else:
            a = '-' + str(x)[1:][::-1]
        reverse_x = int(a)
        if reverse_x < -2**31 or reverse_x > 2**31 - 1:
            return 0
        return reverse_x
        

        
        