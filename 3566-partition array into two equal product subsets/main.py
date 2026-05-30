class Solution(object):
    def checkEqualPartitions(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # pre-process
        L = 2 ** len(nums)

        # helper function
        def valid(mask):
            product, product2 = 1, 1
            idx = 0
            while mask:
                if mask & 1:
                   product *= nums[idx]
                else:
                    product2 *= nums[idx]
                mask >>= 1
                idx += 1
            if product == target and product2 == target:
                return True
            else:
                return False

        # process
        product = 1
        for num in nums:
            product *= num

        if product != target * target:
            return False

        for mask in range(1, L):
            if valid(mask):
                return True
        return False


nums = [3,1,6,8,4]
target = 24

nums = [2,5,3,7]
target = 15

nums = [1,2,8]
target = 4

nums = [4,2,8,3]
target = 8

solution = Solution()
print(solution.checkEqualPartitions(nums, target))
