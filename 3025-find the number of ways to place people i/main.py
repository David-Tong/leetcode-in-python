class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # pre-process
        # helper function
        # within
        def within(upper_left, down_right, points):
            for point in points:
                if point != upper_left and point != down_right:
                    if upper_left[0] <= point[0] <= down_right[0]:
                        if down_right[1] <= point[1] <= upper_left[1]:
                          return True
            return False

        # process
        ans = 0
        for point in points:
            for other in points:
                if point != other:
                    if point[0] <= other[0] and point[1] >= other[1]:
                        if not within(point, other, points):
                            ans += 1
        return ans


points = [[1,1],[2,2],[3,3]]
points = [[6,2],[4,4],[2,6]]
points = [[3,1],[1,3],[1,1]]

solution = Solution()
print(solution.numberOfPairs(points))
