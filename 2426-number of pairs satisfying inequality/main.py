class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type diff: int
        :rtype: int
        """
        # pre-process
        # convert question
        # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
        # nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff
        # nums[i] = nums1[i] - nums2[i]
        nums = list()
        nums = [num1 - num2 for num1, num2 in zip(nums1, nums2)]
        # print(nums)

        # process
        L = len(nums)
        from sortedcontainers import SortedList
        sl = SortedList()
        ans = 0
        # enumerate right and find the most left satisfying the condition
        # nums[i] <= nums[j] + diff
        for num in nums:
            # search
            target = num + diff
            idx = sl.bisect_right(target)

            # update
            if len(sl) > 0:
                if idx == len(sl):
                    ans += idx
                else:
                    if sl[idx] == target:
                        ans += idx + 1
                    else:
                        ans += idx
            sl.add(num)
        return ans


nums1 = [3,2,5]
nums2 = [2,2,1]
diff = 1

nums1 = [3,-1]
nums2 = [-2,2]
diff = -1

from random import randint
nums1 = [randint(-10 ** 4, 10 ** 4) for _ in range(10 ** 4)]
nums2 = [randint(-10 ** 4, 10 ** 4) for _ in range(10 ** 4)]
diff = randint(1, 10 ** 4)

print(nums1)
print(nums2)
print(diff)

solution = Solution()
print(solution.numberOfPairs(nums1, nums2, diff))
