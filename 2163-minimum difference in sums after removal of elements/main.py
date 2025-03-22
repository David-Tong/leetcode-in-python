class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        presums = [0]
        for num in nums:
            presums.append(presums[-1] + num)
        # print(presums)

        N = len(nums) // 3
        from heapq import heapify, heappush, heappop

        # mini_lefts
        heap = list()
        heapify(heap)
        mini_left = sum(nums[:N])
        mini_lefts = [mini_left]
        total = 0
        for x in range(2 * N):
            heappush(heap, -1 * nums[x])
            if x >= N :
                while len(heap) > N:
                    item = heappop(heap)
                    total -= item
                mini_lefts.append(presums[x + 1] - total)
        # print(mini_lefts)

        # max_rights
        heap = list()
        heapify(heap)
        max_right = sum(nums[2*N:])
        max_rights = [max_right]
        total = 0
        for x in range(L - 1, N - 1, -1):
            heappush(heap, nums[x])
            if x < 2 * N:
                while len(heap) > N:
                    item = heappop(heap)
                    total += item
                max_rights.append(presums[-1] - presums[x] - total)
        max_rights = max_rights[::-1]
        # print(max_rights)

        # process
        ans = float("inf")
        for x in range(N + 1):
            ans = min(ans, mini_lefts[x] - max_rights[x])
        return ans


nums = [3,1,2]
# nums = [7,9,5,8,1,3]
nums = [5,6,7,8,9,110,11,2,1,3,5,1,2,11,23]

solution = Solution()
print(solution.minimumDifference(nums))
