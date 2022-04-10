class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        def doNumber(columnTitle, index, number):
            if index == len(columnTitle):
                return number

            ch = columnTitle[index]
            number = number * 26 + ( ord(ch) - ord('A') + 1)
            return doNumber(columnTitle, index + 1, number)

        return doNumber(columnTitle, 0, 0)


columnTitle = "A"
columnTitle = "AB"
columnTitle = "ZY"
columnTitle = "AAA"

solution = Solution()
print(solution.titleToNumber(columnTitle))
