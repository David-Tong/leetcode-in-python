class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        L = len(complexity)
        for x in range(1, L):
            if complexity[x] <= complexity[0]:
                return 0

        # process
        ans = 1
        for x in range(1, L):
            ans = ans * x % MODULO
        return ans


complexity = [1,2,3]
complexity = [3,3,3,4,4,4]
complexity = [_ for _ in range(1, 10 ** 5)]
print(complexity)

solution = Solution()
print(solution.countPermutations(complexity))
