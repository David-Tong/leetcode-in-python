class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dicts = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                 ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                 ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                 ["", "M", "MM", "MMM"]]

        num = str(num)
        ans = ""
        for idx, digit in enumerate(num):
            ans += dicts[len(num)-idx-1][int(digit)]
        return ans


num = 3
#num = 58
#num = 1994
num = 1990
num = 3999

solution = Solution()
print(solution.intToRoman(num))
