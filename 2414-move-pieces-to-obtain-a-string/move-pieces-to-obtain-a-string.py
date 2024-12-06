class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j, length = 0, 0, len(start)
        while i < length or j < length:
            while i < length and start[i] == '_':
                i+=1
            while j < length and target[j] == '_':
                j+=1
            if i == length or j == length:
                return (i == length and j == length)
            if start[i] != target[j] or start[i] == 'L' and j > i or target[j] == 'R' and j < i:
                return False
            i+=1
            j+=1
        return True
        