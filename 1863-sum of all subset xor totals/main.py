class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.L = len(nums)
        self.xors = list()

        def doXOR(nums, index, xor):
            if index == self.L:
                if xor > 0:
                    self.xors.append(xor)
            else:
                if xor == -1:
                    doXOR(nums, index + 1, nums[index])
                    doXOR(nums, index + 1, -1)
                else:
                    doXOR(nums, index + 1, xor ^ nums[index])
                    doXOR(nums, index + 1, xor)

        doXOR(nums, 0, -1)
        print(self.xors)
        return sum(self.xors)


nums = [1,3]
nums = [5,1,6]
nums = [3,4,5,6,7,8]
nums = [3,3,3]
nums = [2]

solution = Solution()
print(solution.subsetXORSum(nums))
