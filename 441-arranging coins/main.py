class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        def totalCoins(n):
            return (n + 1) * n // 2

        left = 1
        right = n
        while left + 1 < right:
            middle = (left + right) // 2
            total = totalCoins(middle)
            if total < n:
                left = middle + 1
            elif total > n:
                right = middle - 1
            else:
                return middle

        if totalCoins(right) <= n:
            return right
        elif totalCoins(left) <= n:
            return left
        else:
            return left - 1


n = 5
n = 8
#n = 1000

solution = Solution()
print(solution.arrangeCoins(n))
