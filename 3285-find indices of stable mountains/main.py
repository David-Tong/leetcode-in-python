class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        # pre-process
        L = len(height)

        # process
        ans = list()
        idx = 1
        while idx < L:
            if height[idx - 1] > threshold:
                ans.append(idx)
            idx += 1
        return ans


height = [1,2,3,4,5]
threshold = 2

solution = Solution()
print(solution.stableMountains(height, threshold))
