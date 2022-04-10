class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        length = len(heights)

        stack = []
        rights = [length] * length
        for x in range(length):
            while stack and heights[stack[-1]] > heights[x]:
                rights[stack[-1]] = x
                stack.pop()
            stack.append(x)

        stack = []
        lefts = [-1] * length
        for x in range(length - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[x]:
                lefts[stack[-1]] = x
                stack.pop()
            stack.append(x)

        ans = 0
        for x in range(length):
            ans = max(ans, (rights[x] - lefts[x] - 1) * heights[x])
        return ans


heights = [2, 1, 5, 6, 2, 3]
heights = [2, 4]
heights = [1]
heights = [2, 1, 2]

solution = Solution()
print(solution.largestRectangleArea(heights))
