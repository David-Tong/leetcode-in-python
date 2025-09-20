class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        visited = [False] * L

        # process
        ans = 0
        for x in range(L):
            idx = x
            nesting = 0
            while not visited[idx]:
                visited[idx] = True
                nesting += 1
                idx = nums[idx]
            ans = max(ans, nesting)
        return ans


nums = [5,4,0,3,1,6,2]
nums = [0,1,2]

solution = Solution()
print(solution.arrayNesting(nums))
