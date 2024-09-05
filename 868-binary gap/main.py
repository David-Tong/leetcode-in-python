class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        start = -1
        idx = 0

        while n:
            if n & 1:
                if start == -1:
                    start = idx
                else:
                    ans = max(ans, idx - start)
                    idx = start
            n = n >> 1
            idx += 1

        return ans


n = 22
n = 8
n = 5
n = 1000
n = 1
n = 113234623

solution = Solution()
print(solution.binaryGap(n))
