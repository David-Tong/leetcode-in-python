class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        def canReach(target, dist, hour):
            from math import ceil
            total = 0
            for dis in dist[:-1]:
                total += ceil(dis * 1.0 / target)
            total += dist[-1] * 1.0 / target
            if total <= hour:
                return True
            else:
                return False

        left = 1
        right = 10 ** 9

        while left + 1 < right:
            middle = (left + right) // 2
            if canReach(middle, dist, hour):
                right = middle
            else:
                left = middle + 1

        if canReach(left, dist, hour):
            return left
        elif canReach(right, dist, hour):
            return right
        else:
            return -1


dist = [1,3,2]
hour = 6

dist = [1,3,2]
hour = 2.7

dist = [1,3,2]
hour = 1.9

dist = [1,1,100000]
hour = 2.01

solution = Solution()
print(solution.minSpeedOnTime(dist, hour))
