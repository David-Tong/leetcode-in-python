class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # process
        ans = list()
        idx = 0
        while n > 0:
            if n % 10 != 0:
                ans.append(n % 10 * (10 ** idx))
            n = n // 10
            idx += 1
        ans = ans[::-1]
        return ans


n = 537
n = 102
n = 6

solution = Solution()
print(solution.decimalRepresentation(n))
