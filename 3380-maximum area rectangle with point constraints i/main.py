class Solution(object):
    def maxRectangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = len(points)

        # process
        # helper function
        # validate if it is a rectangle
        def validate(rectangle):
            if rectangle[0][0] == rectangle[1][0] and rectangle[0][1] == rectangle[2][1]:
                if rectangle[1][1] == rectangle[3][1] and rectangle[2][0] == rectangle[3][0]:
                    return True
            return False

        # validate whether other points in the rectangele
        def validate2(rectangle, x, y, u, v):
            for z in range(L):
                if z not in (x, y, u, v):
                    if rectangle[0][0] <= points[z][0] <= rectangle[3][0]:
                        if rectangle[0][1] <= points[z][1] <= rectangle[3][1]:
                            return False
            return True

        # get area
        def area(rectangle):
            return (rectangle[3][0] - rectangle[0][0]) * (rectangle[3][1] - rectangle[0][1])

        ans = -1
        for x in range(L):
            for y in range(x + 1, L):
                for u in range(y + 1, L):
                    for v in range(u + 1, L):
                        rectangle = sorted([points[z] for z in [x, y, u, v]])
                        if validate(rectangle):
                            if validate2(rectangle, x, y, u, v):
                                ans = max(ans, area(rectangle))
        return ans


points = [[1,1],[1,3],[3,1],[3,3]]
points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]

solution = Solution()
print(solution.maxRectangleArea(points))
