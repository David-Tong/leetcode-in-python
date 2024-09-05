class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        N = len(stoneValue)

        def take(idx):
            if idx in self.cache:
                return self.cache[idx]

            if idx >= N:
                return 0

            min_max = float("-inf")
            curr = 0
            for x in range(3):
                if idx + x < N:
                    curr += stoneValue[idx + x]
                    min_max = max(min_max, curr - take(idx + x + 1))
            self.cache[idx] = min_max
            return min_max

        from collections import defaultdict
        self.cache = defaultdict(int)

        min_max = take(0)
        if min_max > 0:
            return "Alice"
        elif min_max < 0:
            return "Bob"
        else:
            return "Tie"


values = [1,2,3,7]
values = [1,2,3,-9]
values = [1,2,3,6]
values = [10,22,56,12,3,4,6,18,109,21,56]
values = [-16,14,-3,-17,-1,-5,2,11,10,-14,4,12,-6,-4,-15,-7,-4,-5,11,5,11,16,7]

solution = Solution()
print(solution.stoneGameIII(values))
