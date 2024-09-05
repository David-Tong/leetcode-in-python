class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness = sorted(happiness, reverse=True)
        for idx, happy in enumerate(happiness):
            happiness[idx] = happiness[idx] - idx
            if happiness[idx] < 0:
                happiness[idx] = 0

        ans = sum(happiness[:k])
        return ans


happiness = [1,2,3]
k = 2

happiness = [1,1,1,1]
k = 2

happiness = [2,3,4,5]
k = 1

solution = Solution()
print(solution.maximumHappinessSum(happiness, k))
