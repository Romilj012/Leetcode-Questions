class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if '#' not in s and '#' not in t:
            if s == t:
                return True
        i, j = 0, 0
        # while i < len(s) or j < len(t):
        #     if s[i] == t[j]:
        #         continue
        #     elif s[i] == '#' or t[j] == '#':
        #         s = s[:i-1] + s[i+1:]
        #         t = t[:j-1] + s[j+1:]
        #     i += 1
        #     j += 1
        # return s == t
        def removeHash(string):
            stack = []
            for i in string:
                if i == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return "".join(stack)
        if removeHash(s) == removeHash(t):
            return True
        return False


          
            


