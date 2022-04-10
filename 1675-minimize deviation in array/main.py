class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        heap = [-1 * num if num % 2 == 0 else -2 * num for num in nums]
        heapq.heapify(heap)

        maxi = max(heap)
        mini = min(heap)
        ans = maxi - mini

        while True:
            mini = heapq.heappop(heap)
            ans = min(ans, maxi - mini)

            if mini & 1 == 1:
                break

            mini >>= 1
            maxi = max(maxi, mini)
            heapq.heappush(heap, mini)

        return ans


nums = [1, 2, 3, 4]
#nums = [4, 1, 5, 20, 3]
#nums = [2, 10, 8]
nums = [9, 4, 3, 6, 2]
nums = [3, 5]

solution = Solution()
print(solution.minimumDeviation(nums))





