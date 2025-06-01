class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        l = 0
        while n:
            l += 1
            n >>= 1

        # process
        x = 1
        ans = 0
        for _ in range(l):
            ans += x
            x <<= 1
        return ans


n = 5
n = 10
n = 3

solution = Solution()
print(solution.smallestNumber(n))
