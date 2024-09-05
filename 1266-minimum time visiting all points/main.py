class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        L = len(points)

        ans = 0
        for x in range(1, L):
            ans += max(abs(points[x][0] - points[x - 1][0]), abs(points[x][1] - points[x - 1][1]))
        return ans


points = [[1,1],[3,4],[-1,0]]
points = [[3,2],[-2,2]]
points = [[8,9]]

solution = Solution()
print(solution.minTimeToVisitAllPoints(points))
