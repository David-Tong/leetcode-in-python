class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        left1, left2 = 0, 0
        right = 0
        from collections import defaultdict
        dict1, dict2 = defaultdict(int), defaultdict(int)
        count1, count2 = 0, 0

        # process
        ans = 0
        while right < L:
            if nums[right] not in dict1:
                count1 += 1
            dict1[nums[right]] += 1
            if nums[right] not in dict2:
                count2 += 1
            dict2[nums[right]] += 1

            while count1 > k:
                dict1[nums[left1]] -= 1
                if dict1[nums[left1]] == 0:
                    count1 -= 1
                    del dict1[nums[left1]]
                left1 += 1
            while count2 > k - 1:
                dict2[nums[left2]] -= 1
                if dict2[nums[left2]] == 0:
                    count2 -= 1
                    del dict2[nums[left2]]
                left2 += 1

            right += 1
            if count1 == k and count2 == k - 1:
                ans += left2 - left1
        return ans


nums = [1,2,1,2,3]
k = 2

nums = [1,2,1,3,4]
k = 3

solution = Solution()
print(solution.subarraysWithKDistinct(nums, k))
