class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # pre-process
        pt = set()
        for point in points:
            pt.add(point[0])

        # process
        pt = sorted(pt)
        ans = 0
        for x in range(len(pt) - 1):
            ans = max(ans, pt[x + 1] - pt[x])
        return ans


points = [[8,7],[9,9],[7,4],[9,7]]
points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
points = [[1,1],[2,1],[3,0],[11,3],[8,200]]

solution = Solution()
print(solution.maxWidthOfVerticalArea(points))
