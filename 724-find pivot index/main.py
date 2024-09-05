class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixes = list()
        prefix = 0
        prefixes.append(prefix)

        for num in nums:
            prefix += num
            prefixes.append(prefix)

        total = prefix
        for idx, num in enumerate(nums):
            if total - prefixes[idx] - num == prefixes[idx]:
                return idx
        return -1


nums = [1,7,3,6,5,6]
nums = [1,2,3]
nums = [2,1,-1]
nums = [0,0,0,0,0,0]

solution = Solution()
print(solution.pivotIndex(nums))
