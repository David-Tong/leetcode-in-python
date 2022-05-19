class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        from math import log, ceil
        base = minutesToTest // minutesToDie + 1
        number = int(ceil(log(buckets) / log(base)))
        return number


buckets = 1000
minutesToDie = 15
minutesToTest = 60

buckets = 4
minutesToDie = 15
minutesToTest = 15

solution = Solution()
print(solution.poorPigs(buckets, minutesToDie, minutesToTest))