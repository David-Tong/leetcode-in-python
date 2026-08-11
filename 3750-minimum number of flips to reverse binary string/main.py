class Solution(object):
    def minimumFlips(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        bins = list()
        while n:
            bins.append(n & 1)
            n >>= 1
        reversed = bins[::-1]

        # process
        ans = 0
        idx = 0
        while idx < len(bins):
            ans += bins[idx] ^ reversed[idx]
            idx += 1
        return ans


n = 7
n = 10
n = 1000000000

solution = Solution()
print(solution.minimumFlips(n))
