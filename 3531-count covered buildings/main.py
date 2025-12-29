class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        x_tops, x_bottoms = defaultdict(int), defaultdict(int)
        y_lefts, y_rights = defaultdict(int), defaultdict(int)
        for building in buildings:
            x, y = building
            x_tops[x] = max(x_tops[x], y) if x in x_tops else y
            x_bottoms[x] = min(x_bottoms[x], y) if x in x_bottoms else y
            y_rights[y] = max(y_rights[y], x) if y in y_rights else x
            y_lefts[y] = min(y_lefts[y], x) if y in y_lefts else x

        # process
        ans = 0
        for building in buildings:
            x, y = building
            if y_lefts[y] < x < y_rights[y]:
                if x_bottoms[x] < y < x_tops[x]:
                    ans += 1
        return ans


n = 3
buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]

n = 3
buildings = [[1,1],[1,2],[2,1],[2,2]]

n = 5
buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]

solution = Solution()
print(solution.countCoveredBuildings(n, buildings))
