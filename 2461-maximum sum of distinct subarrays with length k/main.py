class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        from collections import defaultdict
        dicts = defaultdict(int)
        total = 0
        for x in range(k):
            dicts[nums[x]] += 1
            total += nums[x]
        repeated = set()
        for num in dicts:
            if dicts[num] > 1:
                repeated.add(num)

        # process
        ans = 0
        for x in range(L - k + 1):
            # move forward
            if x != 0:
                previsous, next = x - 1, x + k - 1
                total = total - nums[previsous] + nums[next]
                dicts[nums[previsous]] -= 1
                if dicts[nums[previsous]] == 1:
                    if nums[previsous] in repeated:
                        repeated.remove(nums[previsous])
                dicts[nums[next]] += 1
                if dicts[nums[next]] > 1:
                    repeated.add(nums[next])

            if not repeated:
                ans = max(ans, total)
        return ans


nums = [1,5,4,2,9,9,9]
k = 3

nums = [4,4,4]
k = 3

solution = Solution()
print(solution.maximumSubarraySum(nums, k))
