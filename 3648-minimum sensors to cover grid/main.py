class Solution(object):
    def minSensors(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        # pre-process
        size = 2 * k + 1
        if n % size == 0:
            row = n // size
        else:
            row = n // size + 1
        if m % size == 0:
            col = m // size
        else:
            col = m // size + 1

        # process
        ans = row * col
        return ans


n = 5
m = 5
k = 1

n = 2
m = 2
k = 2

solution = Solution()
print(solution.minSensors(n, m, k))
