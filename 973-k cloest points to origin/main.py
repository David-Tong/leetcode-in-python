class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def euclideanDistance(point):
            from math import sqrt
            return sqrt(point[0] ** 2 + point[1] ** 2)

        tuples = []
        for point in points:
            tuples.append((point, euclideanDistance(point)))

        tuples = sorted(tuples, key=lambda x: x[1])
        ans = []
        for tuple in tuples[:k]:
            ans.append(tuple[0])
        return ans


points = [[1,3],[-2,2]]
k = 1

points = [[3,3],[5,-1],[-2,4]]
k = 2

solution = Solution()
print(solution.kClosest(points, k))
