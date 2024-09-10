class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        def getSatisfactionTotal(idx, satisfaction):
            total = 0
            for idx, satis in enumerate(satisfaction[idx:]):
                total += (idx + 1) * satis
            return total

        satisfaction = sorted(satisfaction)

        ans = 0
        for idx, satis in enumerate(satisfaction):
            total = getSatisfactionTotal(idx, satisfaction)
            ans = max(ans, total)
            if satis >= 0:
                break
        return ans


satisfaction = [-1,-8,0,5,-9]
satisfaction = [4,3,2]
satisfaction = [-1,-4,-5]

solution = Solution()
print(solution.maxSatisfaction(satisfaction))
