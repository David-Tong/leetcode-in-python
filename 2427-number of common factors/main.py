class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        limit = max(a, b) / 2

        ans = 0
        for x in range(limit):
            if a % (x + 1) == 0 and b % (x + 1) == 0:
                ans += 1
        return ans


a = 12
b = 6

a = 25
b = 30

solution = Solution()
print(solution.commonFactors(a, b))