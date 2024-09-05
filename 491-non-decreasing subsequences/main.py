class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        L = len(nums)
        self.anses = list()

        def doSubsequences(sequence, index, nums):
            if index <= L:
                if len(sequence) > 1:
                    if sequence not in self.anses:
                        self.anses.append(sequence)

            if index < L:
                if len(sequence) > 0:
                    if sequence[-1] <= nums[index]:
                        doSubsequences(sequence + [nums[index]], index + 1, nums)
                else:
                    doSubsequences(sequence + [nums[index]], index + 1, nums)

                doSubsequences(sequence, index + 1, nums)

        doSubsequences(list(), 0, nums)
        return self.anses


nums = [4,6,7,7]
nums = [4,4,3,2,1]
nums = [1]
nums = [2,2,2,2,2,2,2,2]
nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

solution = Solution()
print(solution.findSubsequences(nums))
