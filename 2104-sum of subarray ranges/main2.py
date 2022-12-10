class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        # maxi_counts[x][0] - the number of num less than nums[x] in its right
        #            [x][1] - the number of num less than nums[x] in its left
        maxi_counts = [[1] * 2 for _ in range(L)]
        mini_counts = [[1] * 2 for _ in range(L)]

        maxi_stack = list()
        mini_stack = list()
        for idx in range(L):
            num = nums[idx]
            while maxi_stack and maxi_stack[-1][1] < num:
                idx2, _ = maxi_stack.pop()
                maxi_counts[idx2][0] += (idx - idx2 - 1)
            maxi_stack.append((idx, num))

            while mini_stack and mini_stack[-1][1] > num:
                idx2, _ = mini_stack.pop()
                mini_counts[idx2][0] += (idx - idx2 - 1)
            mini_stack.append((idx, num))

        while maxi_stack:
            idx2, _ = maxi_stack.pop()
            maxi_counts[idx2][0] += (L - idx2 - 1)

        while mini_stack:
            idx2, _ = mini_stack.pop()
            mini_counts[idx2][0] += (L - idx2 - 1)

        maxi_stack = list()
        mini_stack = list()
        for idx in range(L - 1, -1, -1):
            num = nums[idx]
            while maxi_stack and maxi_stack[-1][1] <= num:
                idx2, _ = maxi_stack.pop()
                maxi_counts[idx2][1] += (idx2 - idx - 1)
            maxi_stack.append((idx, num))

            while mini_stack and mini_stack[-1][1] >= num:
                idx2, _ = mini_stack.pop()
                mini_counts[idx2][1] += (idx2 - idx - 1)
            mini_stack.append((idx, num))

        while maxi_stack:
            idx2, _ = maxi_stack.pop()
            maxi_counts[idx2][1] += idx2

        while mini_stack:
            idx2, _ = mini_stack.pop()
            mini_counts[idx2][1] += idx2

        print(maxi_counts)
        print(mini_counts)

        ans = 0
        for x in range(L):
            ans += (maxi_counts[x][0] * maxi_counts[x][1] - mini_counts[x][0] * mini_counts[x][1]) * nums[x]
        return ans


nums = [1,2,3]
nums = [1,3,3]
nums = [4,-2,-3,4,1]

solution = Solution()
print(solution.subArrayRanges(nums))
