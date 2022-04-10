class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        lefts = [0] * N
        rights = [0] * N
        lefts[0] = height[0]
        rights[N - 1] = height[N - 1]

        for x in range(1, N):
            lefts[x] = max(lefts[x-1], height[x])
        for x in range(N - 2, 0, -1):
            rights[x] = max(rights[x+1], height[x])

        ans = 0
        for x in range(N):
            ans += max(0, min(lefts[x], rights[x]) - height[x])
        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [4, 2, 0, 3, 2, 5]
height = [1]

solution = Solution()
print(solution.trap(height))
