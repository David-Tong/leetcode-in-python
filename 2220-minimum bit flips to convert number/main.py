from inspect import stack


class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        xor = start ^ goal

        ans = 0
        while xor:
            ans += xor & 1
            xor >>= 1
        return ans


start = 10
goal = 7

start = 3
goal = 4

solution = Solution()
print(solution.minBitFlips(start, goal))
