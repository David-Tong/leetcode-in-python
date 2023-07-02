class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        L = len(nums)
        HALF = L // 2

        def countTotal(nums, num):
            total = 0
            for shift in range(len(nums)):
                if num >> shift & 1:
                    total += nums[shift]
            return total

        # pre-process
        first_half_nums = nums[:HALF]
        last_half_nums = nums[HALF:]

        # first half
        first_half = set()
        FIST_HALF = len(first_half_nums)
        for num in range(2 ** FIST_HALF):
            first_total = countTotal(first_half_nums, num)
            first_half.add(first_total)

        # last half
        last_half = set()
        LAST_HALF = len(last_half_nums)
        for num in range(2 ** LAST_HALF):
            last_total = countTotal(last_half_nums, num)
            last_half.add(last_total)
        last_half = sorted(last_half)

        from bisect import bisect_left

        ans = float("inf")
        for first_total in first_half:
            target = goal - first_total
            idx = bisect_left(last_half, target)
            if idx == 0:
                last_total = last_half[0]
            elif idx == len(last_half):
                last_total = last_half[-1]
            else:
                if target - last_half[idx - 1] <= last_half[idx] - target:
                    last_total = last_half[idx - 1]
                else:
                    last_total = last_half[idx]
            ans = min(ans, abs(goal - first_total - last_total))
        return ans


nums = [5,-7,3,5]
goal = 6

nums = [7,-9,15,-2]
goal = -5

nums = [1,2,3]
goal = -7

nums = list()
for x in range(40):
    from random import randint
    nums.append(randint(-10 ** 7, 10 ** 7))
goal = randint(-10 ** 9, 10 ** 9)

#print(nums)
#print(goal)

nums = [-2772,6927,4773,-2687,7167,-8995,2940,8869,526]
goal = 969621127

nums = [-2772,6927,4773]
goal = 969621127

solution = Solution()
print(solution.minAbsDifference(nums, goal))
