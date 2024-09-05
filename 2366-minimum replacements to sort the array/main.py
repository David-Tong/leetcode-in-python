class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)

        ans = 0
        mini = nums[-1]
        for x in range(L - 2, -1, -1):
            if nums[x] > mini:
                remainder = nums[x] % mini
                if remainder == 0:
                    slots = nums[x] // mini
                else:
                    slots = nums[x] // mini + 1
                mini = nums[x] // slots
                ans += slots - 1
            else:
                mini = nums[x]
        return ans


nums = [3,9,3]
nums = [1,2,3,4,5]
nums = [3,5,6,7,2,3,4,5,1,2]
nums = [5]
nums = [10,9,8,7,6,5,4,3,2,1]
nums = [4,5,6,3,1,2,4,5,2,1,3,5,6,7,8,9,1,1,5,234,12,41,34]
nums = [12,9,7,6,17,19,21]

solution = Solution()
print(solution.minimumReplacement(nums))
