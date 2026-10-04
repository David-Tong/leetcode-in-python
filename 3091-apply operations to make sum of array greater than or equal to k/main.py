class Solution(object):
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        # process
        from math import ceil

        # support we increase it to x
        # we should have k / x elements in the array
        # it will x - 1 steps to increase it to N, and (k / x - 1) steps to duplicate
        ans = float("inf")
        for x in range(k):
            ans = min(ans, int(x + ceil(k * 1.0 / (x + 1)) - 1))
        return ans


k = 11
k = 1

solution = Solution()
print(solution.minOperations(k))
