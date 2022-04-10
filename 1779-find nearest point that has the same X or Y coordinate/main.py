class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        mini = float("inf")
        ans = -1
        for idx, point in enumerate(points):
            if point[0] == x or point[1] == y:
                distance = abs(x - point[0]) + abs(y - point[1])
                if distance < mini:
                    mini = distance
                    ans = idx
        return ans


x = 3
y = 4
points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]

x = 3
y = 4
points = [[3, 4]]

x = 3
y = 4
points = [[2, 3]]

solution = Solution()
print(solution.nearestValidPoint(x, y, points))
