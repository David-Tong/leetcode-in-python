class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        points = sorted(points, reverse=True)

        from collections import defaultdict
        slopes = defaultdict(float)

        for x in range(N):
            for y in range(x + 1, N):
                if points[x][0] - points[y][0] == 0:
                    slope = float("inf")
                    intercept = points[x][0]
                else:
                    slope = float(points[x][1] - points[y][1]) / float(points[x][0] - points[y][0])
                    intercept = points[x][1] - slope * points[x][0]
                if slope not in slopes:
                    slopes[slope] = defaultdict(set)
                    if intercept not in slopes[slope]:
                        slopes[slope][intercept] = set()

                slopes[slope][intercept].add((points[x][0], points[x][1]))
                slopes[slope][intercept].add((points[y][0], points[y][1]))

        ans = 1
        for slope in slopes:
            for intercept in slopes[slope]:
                ans = max(ans, len(slopes[slope][intercept]))
        return ans


points = [[1,1],[2,2],[2,3],[3,3]]
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
#points = [[3,3],[1,4],[1,1],[2,1],[2,2]]
#points = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]

solution = Solution()
print(solution.maxPoints(points))
