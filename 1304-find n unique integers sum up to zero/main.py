class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # process
        L = n // 2
        ans = list()
        for x in range(L):
            ans.append(x + 1)
            ans.append((x + 1) * -1)
        if n % 2 == 1:
            ans.append(0)
        return ans


n = 5

solution = Solution()
print(solution.sumZero(n))
