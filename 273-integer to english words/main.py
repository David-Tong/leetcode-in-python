class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.ONES = ["", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine"]
        self.TENS = ["", " Ten", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]
        self.TWENTIES = [" Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
        self.UNITS = ["", " Thousand", " Million", " Billion"]

        def getTens(tens):
            number = int(tens)
            ans = ""
            if number == 0:
                pass
            elif number < 10:
                ans = self.ONES[number]
            elif number < 20:
                ans = self.TWENTIES[number - 10]
            elif number < 100:
                ans = self.TENS[int(tens[0])] + self.ONES[int(tens[1])]
            return ans

        def getHundreds(hundred):
            return self.ONES[int(hundred)] + " Hundred"

        def changeToWords(num, unit):
            L = len(num)
            if L >= 3:
                digits = num[L-3:L]
            else:
                digits = num[:L]
            number = int(str(digits))

            ans = ""
            if number == 0:
                if L < 3:
                    if unit == 0:
                        ans = " Zero"
            elif number < 10:
                ans += getTens(digits[-1])
            elif number < 100:
                ans += getTens(digits[-2:])
            else:
                ans += getHundreds(digits[0]) + getTens(digits[1:])

            if unit >= 1:
                if len(ans) > 0:
                    ans += self.UNITS[unit]

            if len(num) > 3:
                ans = changeToWords(num[:L-3], unit + 1) + ans

            return ans

        ans = changeToWords(str(num), 0)
        return ans[1:]

num = 123
num = 12345
#num = 1234567
#num = 0
#num = 11
#num = 99
#num = 2001
num = 2021
num = 2321
num = 2001
num = 2000
num = 999999990
num = 1101101100
num = 200011000
num = 111
num = 111112
num = 100
#num = 1000000
num = 2000200


solution = Solution()
print(solution.numberToWords(num))
