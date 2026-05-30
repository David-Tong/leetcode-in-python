class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        # pre-process
        def getPoints(start, home):
            points = set()
            mini, maxi = min(start, home), max(start, home)
            for x in range(mini, maxi + 1):
                points.add(x)
            return points

        # process
        row_points = getPoints(startPos[0], homePos[0])
        column_points = getPoints(startPos[1], homePos[1])

        ans = 0
        for point in row_points:
            ans += rowCosts[point]
        for point in column_points:
            ans += colCosts[point]
        ans -= rowCosts[startPos[0]]
        ans -= colCosts[startPos[1]]
        return ans


startPos = [1, 0]
homePos = [2, 3]
rowCosts = [5, 4, 3]
colCosts = [8, 2, 6, 7]

startPos = [0, 0]
homePos = [0, 0]
rowCosts = [5]
colCosts = [26]

solution = Solution()
print(solution.minCost(startPos, homePos, rowCosts, colCosts))
