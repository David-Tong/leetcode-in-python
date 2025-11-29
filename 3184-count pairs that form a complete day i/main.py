class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        # pre-process
        counts = [0] * 24
        for hour in hours:
            mod = hour % 24
            counts[mod] += 1
        print(counts)

        # process
        ans = 0
        for x in range(24):
            if x == 0 or x == 12:
                ans += counts[x] * (counts[x] - 1) // 2
            elif x < 12:
                ans += counts[x] * counts[24 - x]
        return ans


hours = [12,12,30,24,24]
hours = [72,48,24,3]

from random import randint
hours = [randint(1, 10 ** 5) for _ in range(5 * 10 ** 4)]
print(hours)

solution = Solution()
print(solution.countCompleteDayPairs(hours))