class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for num in nums:
            if not ans:
                ans = [num, 1]
            else:
                if num == ans[0]:
                    ans[1] += 1
                else:
                    ans[1] -= 1
                    if ans[1] == 0:
                        ans = []
        return ans[0]


nums = [3, 2, 3]
#nums = [2, 2, 1, 1, 1, 2, 2]
#nums = [1]
#nums = [6, 5, 5]
solution = Solution()

print(solution.majorityElement(nums))
