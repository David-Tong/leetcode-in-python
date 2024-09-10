class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * 2 * n
        for x in range(n):
            ans[2 * x] = nums[x]
            ans[2 * x + 1] = nums[x + n]
        return ans


nums = [2,5,1,3,4,7]
n = 3

nums = [1,2,3,4,4,3,2,1]
n = 4

nums = [1,1,2,2]
n = 2

nums = [1,1]
n = 1

solution = Solution()
print(solution.shuffle(nums, n))
