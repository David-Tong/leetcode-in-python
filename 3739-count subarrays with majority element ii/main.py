class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # prefix sum: +1 for target, -1 otherwise
        pres = 0

        # maintain a sorted list of prefix sums
        ordered_presums = [0]

        ans = 0

        from bisect import bisect_left, insort
        for num in nums:
            pres += 1 if num == target else -1

            # count how many previous prefix sums < current pres
            idx = bisect_left(ordered_presums, pres)
            ans += idx

            # insert current prefix sum into sorted structure
            insort(ordered_presums, pres)

        return ans


nums = [1,2,2,3]
target = 2

nums = [1,1,1,1]
target = 1

nums = [1,2,3]
target = 4

from random import choice
nums = [choice([1, 2]) for _ in range(10 ** 5)]
target = 1

print(nums)

solution = Solution()
print(solution.countMajoritySubarrays(nums, target))
