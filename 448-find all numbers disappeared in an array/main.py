class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def swap(x, y):
            if nums[x] != nums[y]:
                nums[x], nums[y] = nums[y], nums[x]
                return True
            else:
                return False

        count = 0
        for idx, num in enumerate(nums):
            while nums[idx] != idx + 1:
                if swap(idx, nums[idx] - 1):
                    pass
                else:
                    break

        ans = list()
        for idx, num in enumerate(nums):
            if num != idx + 1:
                ans.append(idx + 1)

        return ans


nums = [4,3,2,7,8,2,3,1]
nums = [1,1]
nums = [1,3,4,5,6,7,9,9,1,1,2,10]

solution = Solution()
print(solution.findDisappearedNumbers(nums))
