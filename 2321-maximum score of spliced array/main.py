class Solution(object):
    def maximumsSplicedArray(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # pre-process
        # maxScore - get maximum score for nums1 and nums2
        def maxScore(nums1, nums2):
            # convert the problem to find minimal array sum for nums1 - nums2
            L = len(nums1)
            total1, total2 = sum(nums1), sum(nums2)
            nums = list()
            for x in range(L):
                nums.append(nums1[x] - nums2[x])
            # print(nums)

            # process
            # dp init
            # dp[x] - the minimal array sum ended with xth in nums
            dp = [0] * L
            if nums[0] < 0:
                dp[0] = nums[0]

            # dp transfer
            # dp[x] - min(0, dp[x - 1]
            for x in range(1, L):
                dp[x] = min(0, dp[x - 1] + nums[x])
            # print(dp)
            delta = min(dp)

            # post-process
            res = max(total1 - delta, total2 + delta)
            return res

        # process
        ans = max(maxScore(nums1, nums2), maxScore(nums2, nums1))
        return ans


nums1 = [60,60,60]
nums2 = [10,90,10]

nums1 = [20,40,20,70,30]
nums2 = [50,20,50,40,20]

nums1 = [7,11,13]
nums2 = [1,1,1]

nums1 = [1,1,1]
nums2 = [7,11,13]

nums1 = [10,20,50,15,30,10]
nums2 = [40,20,10,100,10,10]

"""
nums1 = [40,20,10,100,10,10]
nums2 = [10,20,50,15,30,10]
"""

solution = Solution()
print(solution.maximumsSplicedArray(nums1, nums2))
