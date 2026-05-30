class Solution(object):
    def minimumPossibleSum(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7

        # helper function
        def getSum(start, end):
            return (start + end) * (end - start + 1) // 2

        # process
        # add the first half
        ans = 0
        half = target // 2
        if n <= half:
            ans = getSum(1, n)
        else:
            ans += getSum(1, half)
            # add the second half
            ans += getSum(target, target + (n - half) - 1)
        ans %= MODULO
        return ans


n = 2
target = 3

n = 3
target = 3

n = 1
target = 1

n = 13
target = 50

solution = Solution()
print(solution.minimumPossibleSum(n, target))
