class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        # process
        # assume x(n) = 111..1, then x(n+1) = 10 * x(n) + 1
        # so if x(n) = k * q + r, then x(n+1) = 10 * k * q + 10 * r + 1
        # so (10 * r + 1) % k will be the new remainder for x(n+1)
        remainders = set()

        x = 1
        remainder = x % k
        ans = 1
        while remainder not in remainders:
            if remainder == 0:
                return ans
            remainders.add(remainder)
            remainder = (10 * remainder + 1) % k
            ans += 1
        return -1


k = 1
k = 2
k = 3
k = 121
k = 100000

solution = Solution()
print(solution.smallestRepunitDivByK(k))
