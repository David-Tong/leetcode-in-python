class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def doCombination(selections, unselections, candidates, target):
            if len(candidates) <= 0:
                return
            if sum(candidates) < target:
                return
            if candidates[0] > target:
                return

            if target == candidates[0]:
                ans = []
                ans.extend(selections)
                ans.append(candidates[0])
                self.anses.append(ans)
            else:
                if candidates[0] not in unselections:
                    selections.append(candidates[0])
                    doCombination(selections[:], unselections[:], candidates[1:], target - candidates[0])
                    selections.pop()
                unselections.append(candidates[0])
                doCombination(selections[:], unselections[:], candidates[1:], target)

        self.anses = []
        candidates = sorted(candidates)
        doCombination([], [], candidates, target)
        return self.anses


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

#candidates = [2, 5, 2, 1, 2]
#target = 5

#candidates = [1]
#target = 2

#candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#target = 27

candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 30

candidates = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
target = 27

solution = Solution()
print(solution.combinationSum2(candidates, target))
