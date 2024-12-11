class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        neg = False
        if numerator*denominator < 0:
            neg = True
        if numerator == 0:
            return "0"
        if numerator % denominator == 0:
            return str(numerator // denominator)
        numerator = abs(numerator)
        denominator = abs(denominator)
        num = []
        output = ""
        output += str(numerator // denominator)
        output += "."
        while True:
            rem = numerator % denominator
            if rem == 0:
                for element in num:
                    output += str(element[-1])
                break
            numerator = rem*10
            q = numerator // denominator
            if [numerator, q] not in num:
                num.append([numerator, q])
            elif [numerator, q] in num:
                ind = num.index([numerator, q])
                for element in num[:ind]:
                    output += str(element[-1])
                output += "("
                for element in num[ind:]:
                    output += str(element[-1])
                output+= ")"
                break
        return "-"+output if neg else output
        