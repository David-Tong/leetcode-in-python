class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        sort = [num for num in nums]
        from collections import deque
        radixes = [deque() for _ in range(10)]

        for x in range(10):
            # put into radix bucket
            for item in sort:
                item = str(item)
                if x < len(item):
                    radix = int(item[len(item)-x-1])
                else:
                    radix = 0
                radixes[radix].append(item)

            # sort
            idx = 0
            for radix in radixes:
                while radix:
                    sort[idx] = radix.popleft()
                    idx += 1

        ans = 0
        for x in range(1, len(sort)):
            ans = max(ans, int(sort[x]) - int(sort[x-1]))
        return ans


nums = [3,6,9,1]
#nums = [11, 25, 136, 1, 9, 9811]
nums = [10]

solution = Solution()
print(solution.maximumGap(nums))