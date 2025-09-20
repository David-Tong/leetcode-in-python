class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return sorted(range(1, n + 1), key=lambda x: bin(x)[:1:-1])


n = 5

solution = Solution()
print(solution.beautifulArray(n))