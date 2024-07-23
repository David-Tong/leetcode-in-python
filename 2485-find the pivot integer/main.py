class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        # binary search
        total = (n + 1) * n // 2
        left = 1
        right = n

        while left + 1 < right:
            middle = (left + right) // 2
            pivot = (middle + 1) * middle // 2
            if pivot < total - pivot + middle:
                left = middle
            elif pivot > total - pivot + middle:
                right = middle
            else:
                return middle

        pivot = (left + 1) * left // 2
        if pivot == total - pivot + left:
            return left
        pivot = (right + 1) * right // 2
        if pivot == total - pivot + right:
            return right
        return -1


n = 8
n = 1
n = 4

solution = Solution()
print(solution.pivotInteger(n))
