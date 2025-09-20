class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(heights)

        # process
        ans = [0] * L
        for x in range(L):
            stack = list()
            y = x + 1
            while y < L and heights[x] > heights[y]:
                if not stack or stack[-1] < heights[y]:
                    stack.append(heights[y])
                y += 1
            if y == L:
                ans[x] = len(stack)
            else:
                ans[x] = len(stack) + 1
        print(ans)


heights = [10,6,8,5,11,9]
heights = [5,1,2,3,10]

solution = Solution()
print(solution.canSeePersonsCount(heights))
