class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        from collections import defaultdict
        dicts = defaultdict(int)
        for point in points:
            x, y = point
            dicts[y] += 1
        # print(dicts)

        combinations = defaultdict(int)
        for y in dicts:
            combinations[y] = dicts[y] * (dicts[y] - 1) // 2
        # print(combinations)
        total = sum(combinations.values())

        # process
        ans = 0
        for y in combinations:
            ans = ans + combinations[y] * (total - combinations[y])
        ans //= 2
        ans %= MODULO
        return ans


points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
points = [[0,0],[1,0],[0,1],[2,1]]
points = [[1,0],[2,0],[3,0],[2,2],[3,2],[1,3],[2,3],[3,3],[4,3],[6,3],[4,5]]

solution = Solution()
print(solution.countTrapezoids(points))