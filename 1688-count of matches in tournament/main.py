class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        matches = 0
        teams = n

        while teams > 1:
            if teams % 2 == 0:
                matches += teams // 2
            else:
                matches += teams // 2 + 1
            teams = teams // 2
        return matches


n = 7
n = 14

solution = Solution()
print(solution.numberOfMatches(n))
