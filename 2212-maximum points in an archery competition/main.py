class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        """
        :type numArrows: int
        :type aliceArrows: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(aliceArrows)

        # dfs function
        # arrange(arrows, idx, score, scores)
        self.maxi = 0
        self.arrangement = list()
        def arrange(arrows, idx, score, arrangement):
            if idx == L:
                if arrows > 0:
                    arrangement[-1] += arrows
                if score > self.maxi:
                    self.maxi = score
                    self.arrangement = arrangement
                return

            if arrows > aliceArrows[idx]:
                arrange(arrows - aliceArrows[idx] - 1, idx + 1, score + idx, arrangement + [aliceArrows[idx] + 1])
            arrange(arrows, idx + 1, score, arrangement + [0])

        arrange(numArrows, 0, 0, list())
        ans = self.arrangement
        return ans


numArrows = 9
aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]

numArrows = 3
aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]

numArrows = 100000
aliceArrows = [1000,1000,1000,1000,9000,9990,8880,8881,765,887,1123,56474]


solution = Solution()
print(solution.maximumBobPoints(numArrows, aliceArrows))
