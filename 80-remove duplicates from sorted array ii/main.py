class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicts = {}
        for num in nums:
            if num not in dicts.keys():
                dicts[num] = 1
            else:
                dicts[num] = 2

        index = 0
        for key in sorted(dicts.keys()):
            if dicts[key] == 1:
                nums[index] = key
                index += 1
            elif dicts[key] == 2:
                nums[index] = key
                nums[index + 1] = key
                index += 2
        return index


nums = [1, 1, 1, 2, 2, 3]
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
nums = [1, 1, 1, 1, 1, 2, 3, 5, 5, 5, 5, 5, 5]
solution = Solution()
print(solution.removeDuplicates(nums))
print(nums)

