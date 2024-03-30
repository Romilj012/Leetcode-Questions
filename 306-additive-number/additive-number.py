class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        def helper(first, second, remaining):
            if len(remaining) < max(len(first), len(second)):
                return False
            if (first[0] == '0' and len(first) != 1) or (second[0] == '0' and len(second) != 1):
                return False
            first = int(first)
            second = int(second)
            result = str(first+second)
            lenResult = len(result)
            if len(remaining) < lenResult:
                return False
            if result == remaining[0:lenResult]:
                if len(remaining) == lenResult:
                    return True
                else:
                    first = second
                    second = result
                    remaining = remaining[lenResult:] 
                    return helper(str(first), str(second), remaining)
            return False
        index1 = 0
        for index2 in range(index1+1, len(num)):
            for index3 in range(index2+1, len(num)):
                first = num[index1:index2]
                second = num[index2:index3]
                remaining = num[index3:]
                if helper(first, second, remaining):
                    return True

        