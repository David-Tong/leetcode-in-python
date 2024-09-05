class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        MODULA = 10 ** 9 + 7
        L = len(nums1)

        from bisect import bisect_left
        sorted_nums1 = sorted(nums1)
        maxi = 0
        total = 0
        for idx in range(L):
            absolute = abs(nums1[idx] - nums2[idx])
            total += absolute
            target = bisect_left(sorted_nums1, nums2[idx])
            if target == 0:
                mini = abs(sorted_nums1[target] - nums2[idx])
            elif target == len(sorted_nums1):
                mini = abs(sorted_nums1[target - 1] - nums2[idx])
            else:
                mini = min(abs(sorted_nums1[target - 1] - nums2[idx]), abs(sorted_nums1[target] - nums2[idx]))

            if absolute > mini:
                if absolute - mini > maxi:
                    maxi = absolute - mini

        return (total - maxi) % MODULA


nums1 = [1,7,5]
nums2 = [2,3,5]

nums1 = [2,4,6,8,10]
nums2 = [2,4,6,8,10]

nums1 = [1,10,4,4,2,7]
nums2 = [9,3,5,1,7,4]

nums1 = [1,10,4,4,2,7]
nums2 = [11,3,5,1,7,4]

nums1 = [1]
nums2 = [2]

nums1 = [1,28,21]
nums2 = [9,21,20]

solution = Solution()
print(solution.minAbsoluteSumDiff(nums1, nums2))
