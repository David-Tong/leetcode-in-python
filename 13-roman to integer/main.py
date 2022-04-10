class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                 ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                 ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                 ["", "M", "MM", "MMM", "", "", "", "", "", ""]]

        from collections import defaultdict
        dicts = defaultdict(int)
        for x in range(len(table)):
            for y in range(len(table[0])):
                if table[x][y] != "":
                    value = y * 10 ** x
                    dicts[table[x][y]] = value

        ans = 0
        x = 0
        while x < len(s):
            for y in range(4, 0, -1):
                if s[x:x+y] in dicts:
                    ans += dicts[s[x:x+y]]
                    x += y
                    break
        return ans


s = "III"
s = "LVIII"
s = "MCMXCIV"

solution = Solution()
print(solution.romanToInt(s))
