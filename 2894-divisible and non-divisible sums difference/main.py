class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # process
        divisible, indivisible = 0, 0
        for x in range(n):
            if (x + 1) % m == 0:
                divisible += x + 1
            else:
                indivisible += x + 1
        ans = indivisible - divisible
        return ans


n = 10
m = 3

n = 5
m = 6

n = 5
m = 1

solution = Solution()
print(solution.differenceOfSums(n, m))
