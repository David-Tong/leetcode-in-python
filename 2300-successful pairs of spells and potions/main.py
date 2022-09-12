class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        M = len(spells)
        N = len(potions)
        potions = sorted(potions)
        pairs = [0] * M

        from bisect import bisect_left
        for idx, spell in enumerate(spells):
            if success % spell == 0:
                pivot = success // spell
            else:
                pivot = success // spell + 1
            pairs[idx] = N - bisect_left(potions, pivot)

        return pairs


spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

spells = [3,1,2]
potions = [8,5,8]
success = 16

solution = Solution()
print(solution.successfulPairs(spells, potions, success))
