class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        HALF = L // 2
        TOTAL = sum(nums)

        def countOnesAndTotal(target_nums, num):
            total = 0
            ones = 0
            for shift in range(HALF):
                if num >> shift & 1:
                    total += target_nums[shift]
                    ones += 1
            return ones, total

        # pre-process
        # calculate the last 15 nums
        first_nums = nums[:HALF]
        last_nums = nums[HALF:]
        from collections import defaultdict
        first_dicts = defaultdict(list)
        last_dicts = defaultdict(list)

        for x in range(2 ** HALF):
            ones, total = countOnesAndTotal(first_nums, x)
            first_dicts[ones].append(total)
            ones, total = countOnesAndTotal(last_nums, x)
            last_dicts[ones].append(total)

        # sort last_dicts for binary search
        for ones in last_dicts:
            last_dicts[ones] = sorted(last_dicts[ones])

        # loop first_dicts to find minimal sum difference
        ans = float("inf")
        for ones in first_dicts:
            remain_ones = HALF - ones
            for total_left in first_dicts[ones]:
                target = TOTAL // 2 - total_left
                from bisect import bisect_left
                idx = bisect_left(last_dicts[remain_ones], target)
                if idx == 0:
                    total_right = last_dicts[remain_ones][idx]
                elif idx == len(last_dicts[remain_ones]):
                    total_right = last_dicts[remain_ones][-1]
                else:
                    if last_dicts[remain_ones][idx] - target <= target - last_dicts[remain_ones][idx - 1]:
                        total_right = last_dicts[remain_ones][idx]
                    else:
                        total_right = last_dicts[remain_ones][idx - 1]
                total = total_left + total_right
                other = TOTAL - total
                ans = min(ans, abs(total - other))
        return ans


nums = [3,9,7,3]
nums = [-36,36]
nums = [2,-1,0,4,-2,-9]
nums = [-1,-5,-7,-32,-5,-17,4,5,6,8,9,1,11,23,87,1,2,3,4,5,6,1,12,44,55,6]
nums = [-1,-5,-7,-32,-5,-17,4,5,6,8,9,1,11,23,87,1,2,3,4,5,6,1,12,44,55,6,22,31,-119,-92]
nums = [7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694]

solution = Solution()
print(solution.minimumDifference(nums))
