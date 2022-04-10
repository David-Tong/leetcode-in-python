class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        limits = len(nums) // 3 + 1

        left = 0
        right = 1
        ans = []
        while right < len(nums):
            if nums[right] == nums[left]:
                right += 1
            else:
                if right - left >= limits:
                    ans.append(nums[left])
                left = right
                right += 1

        if right - left >= limits:
            ans.append(nums[left])

        return ans


nums = [3, 2, 3]
nums = [1]
nums = [1, 2]
#nums = [3, 2, 3, 4, 2, 2]

solution = Solution()
print(solution.majorityElement(nums))