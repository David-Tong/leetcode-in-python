class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        mod26 = (columnNumber - 1) % 26
        div26 = (columnNumber - 1) // 26
        ans = chr(ord("A") + mod26)
        while div26:
            mod26 = (div26 - 1) % 26
            div26 = (div26 - 1) // 26
            ans = chr(ord("A") + mod26) + ans
        return ans


columnNumber = 28
columnNumber = 701
columnNumber = 1000
columnNumber = 27
columnNumber = 676
columnNumber = 702

solution = Solution()
print(solution.convertToTitle(columnNumber))
