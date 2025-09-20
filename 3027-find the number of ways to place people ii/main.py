class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # pre-process
        # sort by x asc and y desc
        points = sorted(points, key=lambda point: [point[0], -1 * point[1]])
        print(points)

        # process
        L = len(points)
        ans = 0
        for x in range(L):
            lower, upper = float("-inf"), points[x][1]
            for y in range(x + 1, L):
                if points[y][1] > upper:
                    continue
                if points[y][1] <= lower:
                    continue
                lower = points[y][1]
                ans += 1
        return ans


points = [[1,1],[2,2],[3,3]]
# points = [[1,1],[2,2],[2,3],[3,3]]
points = [[6,2],[4,4],[2,6]]
points = [[3,1],[1,3],[1,1]]

solution = Solution()
print(solution.numberOfPairs(points))
