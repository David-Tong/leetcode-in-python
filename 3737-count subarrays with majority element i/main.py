class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # process
        from collections import defaultdict
        dicts = defaultdict(int)
        dicts[0] = 1
        presums = list()
        presums.append(0)

        ans = 0
        for num in nums:
            if num == target:
                delta = 1
            else:
                delta = -1
            presum = presums[-1] + delta
            for key in dicts:
                if presum - key > 0:
                    ans += dicts[key]
            dicts[presum] += 1
            presums.append(presum)
        return ans


nums = [1,2,2,3]
target = 2

nums = [1,1,1,1]
target = 1

nums = [1,2,3]
target = 4

solution = Solution()
print(solution.countMajoritySubarrays(nums, target))
