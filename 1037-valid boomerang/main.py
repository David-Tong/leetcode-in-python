class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # pre-process
        point, point2, point3 = points

        # conner cases
        if point == point2 or point == point3 or point2 == point3:
            return False

        def slop(point, point2):
            if point2[0] - point[0] == 0:
                return 10 ** 9
            else:
                return (point2[1] - point[1]) * 1.0 / (point2[0] - point[0])

        # process
        # print(slop(point, point2))
        # print(slop(point2, point3))
        return False if abs(slop(point, point2) - slop(point2, point3)) < 1e-5 else True


points = [[1,1],[2,3],[3,2]]
points = [[1,1],[2,2],[3,3]]
points = [[0,0],[1,1],[1,1]]
points = [[0,0],[0,2],[2,1]]
points = [[73,31],[73,19],[73,45]]

solution = Solution()
print(solution.isBoomerang(points))
