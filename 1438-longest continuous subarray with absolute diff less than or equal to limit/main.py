class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        L = len(nums)

        left = 0
        right = 0

        from collections import deque
        min_queue = deque()
        max_queue = deque()

        ans = 0
        while right < L:
            while min_queue and min_queue[-1] > nums[right]:
                min_queue.pop()
            min_queue.append(nums[right])

            while max_queue and max_queue[-1] < nums[right]:
                max_queue.pop()
            max_queue.append(nums[right])

            right += 1

            while max_queue[0] - min_queue[0] > limit:
                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                left += 1

            ans = max(ans, right - left)
        return ans


nums = [8,2,4,7]
limit = 4

nums = [10,1,2,4,7,2]
limit = 5

nums = [4,2,2,2,4,4,2,2]
limit = 0

nums = [1]
limit = 1

solution = Solution()
print(solution.longestSubarray(nums, limit))
