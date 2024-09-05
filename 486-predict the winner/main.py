class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def predict(left, right):
            key = str(left) + "-" + str(right)
            if key in self.cache:
                return self.cache[key]

            if left == right:
                return nums[left]

            min_max = float("-inf")
            # take left
            min_max = max(min_max, nums[left] - predict(left + 1, right))
            # take right
            min_max = max(min_max, nums[right] - predict(left, right - 1))
            self.cache[key] = min_max
            return min_max

        left = 0
        right = len(nums) - 1
        from collections import defaultdict
        self.cache = defaultdict(long)
        return True if predict(left, right) >= 0 else False


nums = [1,5,2]
nums = [1,5,233,7]
nums = [1,5,6,11,234,12,56,7,8,9,21]
nums = [1]
nums = [43,5,6,1,21,234,54,5,6,89,112,123,34,3,6,9,11,0,10000,100]

solution = Solution()
print(solution.PredictTheWinner(nums))
