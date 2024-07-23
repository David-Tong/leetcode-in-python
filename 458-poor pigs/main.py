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
        number = log(buckets) / log(base)
        if number - int(number) < 10 ** -9:
            ans = int(number)
        else:
            ans = int(number) + 1
        return ans


buckets = 4
minutesToDie = 15
minutesToTest = 15

buckets = 4
minutesToDie = 15
minutesToTest = 30

"""
buckets = 1000
minutesToDie = 15
minutesToTest = 60

buckets = 125
minutesToDie = 1
minutesToTest = 4
"""

solution = Solution()
print(solution.poorPigs(buckets, minutesToDie, minutesToTest))