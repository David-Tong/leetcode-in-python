class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        # get differences
        differences = []
        for idx, num in enumerate(nums):
            if idx > 0:
                differences.append(nums[idx] - nums[idx - 1])

        # get intervals
        left = 0
        right = 1
        intervals = []
        while right < len(differences):
            if differences[left] == differences[right]:
                right += 1
            else:
                interval = right - left + 1
                if interval >= 3:
                    intervals.append(interval)
                left = right
                right += 1
        interval = right - left + 1
        if interval >= 3:
            intervals.append(interval)

        ans = 0
        for interval in  intervals:
            for x in range(3, interval + 1):
               ans += (interval - x + 1)
        return ans


nums = [1, 2, 3, 4]
nums = [1]
nums = [1, 2, 3, 4, 5, 3, 1, -1, 0, 1, 2]

solution = Solution()
print(solution.numberOfArithmeticSlices(nums))
