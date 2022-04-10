class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        left = 0
        right = 0
        queue = []
        ans = []
        while right < len(nums):
            num = nums[right]
            while len(queue) > 0 and queue[-1] < num:
                queue.pop(-1)
            queue.append(num)
            right += 1

            if right - left >= k:
                ans.append(queue[0])
                num = nums[left]
                if num == queue[0]:
                    queue.pop(0)
                left += 1
        return ans