class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # pre-process
        L = len(points)
        E = 10 ** -5

        # heron's formula
        from math import sqrt
        def heron(p1, p2, p3):
            a = sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
            b = sqrt((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)
            c = sqrt((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)
            p = ((a + b + c) * 1.0) / 2
            if p - a < E or p - b < E or p -c < E:
                return 0
            else:
                s = sqrt(p * (p - a) * (p - b) * (p - c))
            return s

        # process
        ans = 0
        for x in range(L):
            for y in range(x + 1, L):
                for z in range(y + 1, L):
                    ans = max(ans, heron(points[x], points[y], points[z]))
        return ans


points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
points = [[1,0],[0,0],[0,1]]
points = [[35,-23],[-12,-48],[-34,-40],[21,-25],[-35,-44],[24,1],[16,-9],[41,4],[-36,-49],[42,-49],[-37,-20],[-35,11],[-2,-36],[18,21],[18,8],[-24,14],[-23,-11],[-8,44],[-19,-3],[0,-10],[-21,-4],[23,18],[20,11],[-42,24],[6,-19]]

solution = Solution()
print(solution.largestTriangleArea(points))
