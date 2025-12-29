class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # pre-process
        from math import sqrt
        L = len(points)

        # helper function
        def distance(x, y):
            return (points[x][0] - points[y][0]) ** 2 +  (points[x][1] - points[y][1]) ** 2

        def conlinear(x, y, z):
            return (points[y][1] - points[x][1]) * (points[z][0] - points[x][0]) \
                - (points[z][1] - points[x][1]) * (points[y][0] - points[x][0]) == 0

        def area(x, y, u, v):
            if conlinear(x, y, u) or conlinear(x, y, v) or conlinear(y, u, v):
                return 0

            dists = list()
            dists.append(distance(x, y))
            dists.append(distance(x, u))
            dists.append(distance(x, v))
            dists.append(distance(y, u))
            dists.append(distance(y, v))
            dists.append(distance(u, v))
            dists = sorted(dists)

            if dists[0] == dists[1] and dists[2] == dists[3] and dists[4] == dists[5]:
                if dists[0] + dists[2] == dists[4]:
                    # print(points[x], points[y], points[u], points[v])
                    # print(sqrt(dists[0]) * sqrt(dists[2]))
                    return sqrt(dists[0]) * sqrt(dists[2])

            return 0

        # process
        ans = float('inf')
        for x in range(L):
            for y in range(x + 1, L):
                for u in range(y + 1, L):
                    for v in range(u + 1, L):
                        if area(x, y, u, v) > 0:
                            ans = min(ans, area(x, y, u, v))
        return 0 if ans == float('inf') else ans


points = [[1,2],[2,1],[1,0],[0,1]]
points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
points = [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
points = [[2,4],[4,2],[1,0],[3,4],[4,4],[2,2],[1,1],[3,0],[1,4],[0,3],[0,1],[2,1],[4,0]]
points = [[6995,28840],[35392,23219],[24403,4904],[20000,4275],[4396,21947],[33005,28840],[35708,20731],[35525,22500],[4520,22765],[14900,34875],[35525,17500],[11963,33516],[33516,28037],[20000,35725],[4365,21680],[5796,26747],[35096,24403],[13340,34245],[31500,30725],[30989,31248],[10939,32852],[8752,30989],[33875,27400],[35540,22405],[27315,6080],[26747,5796],[30725,31500],[34960,15155],[28840,33005],[7148,29061],[9275,31500],[18320,35635],[26660,5755],[8685,30920],[5125,25100],[19269,35708],[35604,18053],[33005,11160],[34245,26660],[17595,35540],[29435,7420],[21947,35604],[22500,4475],[34204,26747],[29435,32580],[10565,32580],[28037,33516],[22765,35480],[34204,13253],[22405,35540]]

solution = Solution()
print(solution.minAreaFreeRect(points))
