class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        from collections import defaultdict
        parallels = defaultdict(int)
        for point in points:
            x, y = point
            parallels[y] += 1

        # process
        ans = 0
        count = 0
        for y in parallels:
            if parallels[y] > 1:
                combinations = parallels[y] * (parallels[y] - 1) // 2
                ans = (ans + count * combinations) % MODULO
                count += combinations
        return ans


points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
points = [[0,0],[1,0],[0,1],[2,1]]
points = [[1,0],[2,0],[3,0],[2,2],[3,2],[1,3],[2,3],[3,3],[4,3],[6,3],[4,5]]

solution = Solution()
print(solution.countTrapezoids(points))