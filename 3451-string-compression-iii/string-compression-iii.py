class Solution:
    def compressedString(self, word: str) -> str:
        count = 1
        comp = ""
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                count += 1
                if count == 9:
                    comp += "9" + word[i-1]
                    count = 0
            else:
                if count > 0:
                    comp += str(count) + word[i-1]
                count = 1
        if count > 0:
            comp += str(count) + word[-1]
        return comp
                


        