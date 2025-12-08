class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        L = len(nums)
        diffs = [0] * L
        for request in requests:
            start, end = request
            diffs[start] += 1
            if end < L - 1:
                diffs[end + 1] -= 1

        counts = [0] * L
        count = 0
        idx = 0
        while idx < L:
            count += diffs[idx]
            counts[idx] = count
            idx += 1

        # process
        counts = sorted(counts)
        nums = sorted(nums)
        idx = 0
        ans = 0
        while idx < L:
            ans += (nums[idx] * counts[idx]) % MODULO
            idx += 1
        ans = ans % MODULO
        return ans


nums = [1,2,3,4,5]
requests = [[1,3],[0,1]]

nums = [1,2,3,4,5,6]
requests = [[0,1]]

nums = [1,2,3,4,5,10]
requests = [[0,2],[1,3],[1,1]]

soluton = Solution()
print(soluton.maxSumRangeQuery(nums, requests))
