class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        idx = 0
        upper = n // 2
        for x in range(1, upper + 1):
            if n % x == 0:
                idx += 1
                if idx == k:
                    return x

        if idx == k - 1:
            return n

        return -1


n = 12
k = 3

n = 7
k = 2

n = 4
k = 4

n = 1
k = 1

n = 999
k = 6

n = 2
k = 2

solution = Solution()
print(solution.kthFactor(n, k))
