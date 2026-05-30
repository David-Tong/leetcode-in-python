class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        # helper function
        def reverse(n):
            return int(str(n)[::-1])

        # process
        ans = abs(n - reverse(n))
        return ans


n = 25
n = 10
n = 7

solution = Solution()
print(solution.mirrorDistance(n))
