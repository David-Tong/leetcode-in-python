class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # process
        quotient = k // (n - 1)
        remainder = k % (n - 1)

        ans = 0
        if quotient % 2 == 0:
            ans = remainder
        else:
            ans = (n - 1) - remainder
        return ans


n = 3
k = 5

n = 5
k = 6

n = 4
k = 2

solution = Solution()
print(solution.numberOfChild(n, k))
