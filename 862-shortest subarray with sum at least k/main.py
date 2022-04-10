class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = [0] * (len(nums) + 1)
        for x in range(len(nums)):
            prefix_sum[x+1] = prefix_sum[x] + nums[x]

        from collections import deque
        queue = deque()
        ans = len(nums) + 1
        for idx, x in enumerate(prefix_sum):
            while queue and x <= prefix_sum[queue[-1]]:
                queue.pop()
            while queue and x - prefix_sum[queue[0]] >= k:
                ans = min(ans, idx - queue.popleft())
            queue.append(idx)

        return ans if ans != len(nums) + 1 else -1


nums = [1]
k = 1

nums = [1,2]
k = 4

nums = [2,-1,2]
k = 3

nums = [48, 99, 37, 4, -31]
k = 140

nums = [17,85,93,-45,-21]
k = 150

solution = Solution()
print(solution.shortestSubarray(nums, k))
