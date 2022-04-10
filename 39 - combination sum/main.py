class Solution(object):
    def __init__(self):
        self.combinations = []


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        selection = []
        index = 0
        self.doCombinationSum(candidates, target, selection)
        return self.combinations


    def doCombinationSum(self, candidates, target, selection):
        if target == 0:
            sorted_selection = sorted(selection)
            if sorted(sorted_selection) not in self.combinations:
                self.combinations.append(sorted_selection)
            return
        elif target < 0:
            return

        for candidate in candidates:
            selection.append(candidate)
            self.doCombinationSum(candidates, target - candidate, selection)
            selection.pop()


solution = Solution()
#candidates = [2,3,6,7]
#target = 7

#candidates = [2,3,5]
#target = 8

#candidates = [2]
#target = 1

#candidates = [1]
#target = 1

#candidates = [1]
#target = 2

combinations = solution.combinationSum(candidates, target)
print(combinations)