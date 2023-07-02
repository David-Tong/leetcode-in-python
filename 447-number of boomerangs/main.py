class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        L = len(points)

        def arrangement(n, k):
            from math import factorial
            return factorial(n) / factorial(n - k)

        ans = 0
        for x in range(L):
            from collections import defaultdict
            dicts = defaultdict(int)

            for y in range(L):
                if x != y:
                    distance = (points[y][0] - points[x][0]) ** 2 + (points[y][1] - points[x][1]) ** 2
                    dicts[distance] += 1

            for key in dicts:
                if dicts[key] >= 2:
                    ans += arrangement(dicts[key], 2)
        return ans


points = [[0,0],[1,0],[2,0]]
points = [[1,1],[2,2],[3,3]]
points = [[1,0],[0,1],[-1,0],[0,-1]]
points = [[1,1]]

solution = Solution()
print(solution.numberOfBoomerangs(points))
