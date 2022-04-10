class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        for x in range(1, len(coordinates)):
            if coordinates[x][0] - coordinates[x-1][0] == 0:
                k = float("inf")
            else:
                k = (coordinates[x][1] - coordinates[x - 1][1]) / (coordinates[x][0] - coordinates[x - 1][0])

            if x == 1:
                prev_k = k
            else:
                if prev_k != k:
                    return False
                else:
                    prev_k = k
        return True


coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
#coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
coordinates = [[2,3],[2,5],[2,7]]

solution = Solution()
print(solution.checkStraightLine(coordinates))
