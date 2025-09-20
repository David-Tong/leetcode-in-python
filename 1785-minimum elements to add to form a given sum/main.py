class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        # pre-process
        total = sum(nums)
        gap = abs(goal - total)

        # process
        if gap % limit == 0:
            ans = gap // limit
        else:
            ans = gap // limit + 1
        return ans


nums = [1,-1,1]
limit = 3
goal = -4

nums = [1,-10,9,1]
limit = 100
goal = 0

nums = [1,-1]
limit = 100
goal = 0

solution = Solution()
print(solution.minElements(nums, limit, goal))
