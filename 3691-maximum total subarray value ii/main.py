class RMQ:
    def __init__(self, nums):
        self.n = len(nums)
        self.K = self.n.bit_length()
        self.maxis = [[0] * self.K for _ in range(self.n)]
        self.minis = [[0] * self.K for _ in range(self.n)]

        # k = 0
        for i in range(self.n):
            self.maxis[i][0] = nums[i]
            self.minis[i][0] = nums[i]

        # binary lifting DP
        k = 1
        while (1 << k) <= self.n:
            step = 1 << (k - 1)
            for i in range(self.n - (1 << k) + 1):
                self.maxis[i][k] = max(self.maxis[i][k - 1],
                                       self.maxis[i + step][k - 1])
                self.minis[i][k] = min(self.minis[i][k - 1],
                                       self.minis[i + step][k - 1])
            k += 1

    def score(self, left, right):
        """Return max(nums[left..right]) - min(nums[left..right]) in O(1)."""
        length = right - left + 1
        k = length.bit_length() - 1
        step = 1 << k
        maxi = max(self.maxis[left][k], self.maxis[right - step + 1][k])
        mini = min(self.minis[left][k], self.minis[right - step + 1][k])
        return maxi - mini


class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        - For each left index l, the sequence score(l, r) for r = n-1..l is
          non-increasing.
        - Treat each left's sequence as a sorted list.
        - Use a max-heap to extract the global top-k values across all sequences.
        - Each heap entry is (score, l, r), representing score(l, r).
        - After popping (l, r), push (l, r-1) if r > l.
        """
        import heapq

        n = len(nums)
        rmq = RMQ(nums)

        # Max-heap (store negative values because Python has min-heap)
        pq = []

        # Initialize heap with the maximum score for each left index:
        # score(l, n-1)
        for l in range(n):
            val = rmq.score(l, n - 1)
            heapq.heappush(pq, (-val, l, n - 1))

        ans = 0

        # Extract the top-k scores
        while k > 0:
            negVal, l, r = heapq.heappop(pq)
            val = -negVal
            ans += val
            k -= 1

            # Push the next candidate from this left index:
            # score(l, r-1)
            if r > l:
                newVal = rmq.score(l, r - 1)
                heapq.heappush(pq, (-newVal, l, r - 1))

        return ans


nums = [1,3,2]
k = 2

nums = [4,2,5,1]
k = 3

from random import randint
nums = [randint(1,10 ** 9) for _ in range(5 * 10 ** 4)]
k = 10 ** 5
print(nums)

solution = Solution()
print(solution.maxTotalValue(nums, k))