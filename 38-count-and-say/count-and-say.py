class Solution:
    def countAndSay(self, n: int) -> str:
        #recurrsion method
        if n == 1:
            return "1"
        prev = self.countAndSay(n-1)
        result = ""
        count = 1
        for i in range(len(prev)):
            if i == len(prev)-1 or prev[i] != prev[i+1]:
                result = result + str(count) + prev[i]
                count =1
            else:
                count +=1
        return result
        
        # s = "11"
        # if n ==1 : 
        #     return "1"
        # if n ==2:
        #     return "11"
        # for i in range(2, n):
        #     count = 1 
        #     result = ""
        #     for j in range(len(s)):
        #         if j == len(s)-1:
        #             result = result + str(count) + s[j] 
        #         elif s[j] == s[j+1]:
        #             count += 1
        #         else:
        #             result = result + str(count) + s[j]
        #             count = 1
        #     s = result
        # return result


        
