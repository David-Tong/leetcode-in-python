class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(heights)

        # process
        stack = list()
        ans = [0] * L
        for x in range(L):
            while stack and stack[-1][1] < heights[x]:
                idx, height = stack.pop()
                ans[idx] = x - idx
            stack.append((x, heights[x]))

        print(ans)


heights = [10,6,8,5,11,9]

solution = Solution()
print(solution.canSeePersonsCount(heights))