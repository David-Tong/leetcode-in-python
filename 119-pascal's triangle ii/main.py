class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        previous = [1]
        for row in range(1, rowIndex + 1):
            current = list()
            for col in range(len(previous) + 1):
                item = 0
                if col > 0:
                    item += previous[col - 1]
                if col < len(previous):
                    item += previous[col]
                current.append(item)
            previous = current
        return previous


rowIndex = 3

solution = Solution()
print(solution.getRow(rowIndex))
