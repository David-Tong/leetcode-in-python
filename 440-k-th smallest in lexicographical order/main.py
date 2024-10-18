from FixTk import prefix
from pipes import stepkinds


class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count(prefix, successor):
            counts = 0
            while prefix <= n:
                counts += min(n + 1, successor) - prefix
                prefix *= 10
                successor *= 10
            return counts

        curr = 1
        k -= 1
        while k > 0:
            counts = count(curr, curr + 1)
            if counts <= k:
                curr += 1
                k -= counts
            else:
                curr *= 10
                k -= 1
        return curr


n = 13
k = 2

n = 1
k = 1

n = 13
k = 6

solution = Solution()
print(solution.findKthNumber(n, k))
