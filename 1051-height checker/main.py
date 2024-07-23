class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # pre-process
        L = len(heights)
        expected = sorted(heights)

        # process
        ans = 0
        for x in range(L):
            if expected[x] != heights[x]:
                ans += 1
        return ans


heights = [1,1,4,2,1,3]

solution = Solution()
print(solution.heightChecker(heights))
