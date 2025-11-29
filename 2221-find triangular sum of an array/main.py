class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        from collections import deque
        queue = deque()
        for num in nums:
            queue.append(num)

        # process
        while len(queue) > 1:
            size = len(queue)
            for _ in range(size - 1):
                num = queue.popleft()
                num2 = queue[0]
                queue.append((num + num2) % 10)
            queue.popleft()
        ans = queue[0]
        return ans


nums = [1,2,3,4,5]
nums = [5]

solution = Solution()
print(solution.triangularSum(nums))
