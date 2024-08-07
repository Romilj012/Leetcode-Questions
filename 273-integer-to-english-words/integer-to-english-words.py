class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Define the words for numbers.
        below_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
                    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']

        def wordify(num):
            if num == 0:
                return ''
            elif num < 20:
                return below_20[num] + ' '
            elif num < 100:
                return tens[num // 10] + ' ' + wordify(num % 10)
            else:
                return below_20[num // 100] + ' Hundred ' + wordify(num % 100)

        result = ''
        i = 0

        while num > 0:
            if num % 1000 != 0:
                result = wordify(num % 1000) + thousands[i] + ' ' + result
            num //= 1000
            i += 1

        return result.strip()

            