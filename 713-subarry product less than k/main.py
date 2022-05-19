class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def doSum(left, right):
            total = 0
            for x in range(right - left + 1):
                total += x + 1
            return total

        from collections import defaultdict
        ranges = defaultdict(int)
        product = 1

        left = 0
        right = 0
        while right < len(nums):
            product *= nums[right]
            while left < right and product >= k:
                product //= nums[left]
                left += 1
            # save all longest valid range [left: right + 1] with product less than k
            if product < k:
                ranges[left] = right
            right += 1

        # convert to tuples
        ranges = sorted([(key, ranges[key]) for key in ranges])

        # get answer
        ans = 0
        for idx in range(len(ranges)):
            if idx == 0:
                ans += doSum(ranges[idx][0], ranges[idx][1])
            else:
                ans += doSum(ranges[idx][0], ranges[idx][1]) - doSum(ranges[idx][0], ranges[idx - 1][1])
        return ans


nums = [10,5,2,6]
k = 100

#nums = [10,5,2,6,4]
#k = 100

#nums = [10,5,2,5,10]
#k = 100

#nums = [1,2,3]
#k = 0

nums = [1,7,3,2,8,1,7,1,2,3,8,10]
k = 45

solution = Solution()
print(solution.numSubarrayProductLessThanK(nums, k))
