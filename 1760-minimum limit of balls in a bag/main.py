class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def canDo(target, nums, maxOperations):
            for num in nums:
                if num > target:
                    if num % target == 0:
                        maxOperations -= (num // target - 1)
                    else:
                        maxOperations -= (num // target)
                if maxOperations < 0:
                    return False
            return True

        left = 1
        right = max(nums)

        while left + 1 < right:
            middle = (left + right) // 2
            if canDo(middle, nums, maxOperations):
                right = middle
            else:
                left = middle + 1

        if canDo(left, nums, maxOperations):
            return left
        else:
            return right


nums = [9]
maxOperations = 2

nums = [2,4,8,2]
maxOperations = 4

nums = [1]
maxOperations = 1

solution = Solution()
print(solution.minimumSize(nums, maxOperations))
