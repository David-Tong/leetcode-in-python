class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x: (x[0], x[1]))
        limit = points[0][1]
        ans = 1
        for point in points[1:]:
            if point[0] <= limit:
                limit = min(limit, point[1])
            else:
                limit = point[1]
                ans += 1
        return ans



points = [[10,16],[2,8],[1,6],[7,12]]
#points = [[1,2],[3,4],[5,6],[7,8]]
#points = [[1,2],[2,3],[3,4],[4,5]]
#points = [[10,16],[2,8],[1,6],[7,12],[1,3]]
#points = [[1,1]]
#points = [[1,2],[4,5],[1,5]]
#points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]

solution = Solution()
print(solution.findMinArrowShots(points))
