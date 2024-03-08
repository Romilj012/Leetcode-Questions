class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        s = ""
        thisDict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtracking(i, s):
            if i >= len(digits):
                result.append(s)
                return 
            for c in thisDict[digits[i]]:
                backtracking(i+1, s+c)
                
        if digits:
            backtracking(0, s)
        return result

