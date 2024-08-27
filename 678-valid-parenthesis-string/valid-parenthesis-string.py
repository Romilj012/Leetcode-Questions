class Solution:
    def checkValidString(self, s: str) -> bool:
        check = []
        collectStar = []
        for i, char in enumerate(s):
            if char == "(":
                check.append(i)
            if char == "*":
                collectStar.append(i)
            if char == ")":
                if check:
                    check.pop()
                elif collectStar:
                    collectStar.pop()
                else:
                    return False
        while check and collectStar:
            if check[-1] > collectStar[-1]:
                return False  # '(' cannot be matched with '*' appearing before it
            check.pop()
            collectStar.pop()
        return False if check else True
