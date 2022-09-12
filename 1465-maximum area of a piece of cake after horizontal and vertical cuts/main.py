class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]

        maxHorizontalCut = 0
        for x in range(1, len(horizontalCuts)):
            maxHorizontalCut = max(maxHorizontalCut, horizontalCuts[x] - horizontalCuts[x-1])

        maxVerticalCut = 0
        for x in range(1, len(verticalCuts)):
            maxVerticalCut = max(maxVerticalCut, verticalCuts[x] - verticalCuts[x-1])

        return (maxHorizontalCut * maxVerticalCut) % MOD


h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]

h = 5
w = 4
horizontalCuts = [3,1]
verticalCuts = [1]

h = 5
w = 4
horizontalCuts = [3]
verticalCuts = [3]

h = 1000000000
w = 1000000000
horizontalCuts = [2]
verticalCuts = [2]

solution = Solution()
print(solution.maxArea(h, w, horizontalCuts, verticalCuts))
