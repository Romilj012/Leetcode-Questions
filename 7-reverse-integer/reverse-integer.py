# class Solution:
#     def reverse(self, x: int) -> int:
#         if x >= 0:
#             a = str(x)[::-1]
#         else:
#             a = '-' + str(x)[1:][::-1]
#         reverse_x = int(a)
#         if reverse_x < -2**31 or reverse_x > 2**31 - 1:
#             return 0
#         return reverse_x
        
class Solution:
    def reverse(self, x: int) -> int:
        # Integer.MAX_VALUE = 2147483647 (end with 7)
        # Integer.MIN_VALUE = -2147483648 (end with -8 )

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))  # (python dumb) -1 %  10 = 9
            x = int(x / 10)  # (python dumb) -1 // 10 = -1

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res

        
        