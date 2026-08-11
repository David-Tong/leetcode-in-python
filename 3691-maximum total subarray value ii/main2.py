class RMQ:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
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
        n = len(nums)
        rmq = RMQ(nums)

        # helper: count subarrays with score >= target
        def count_ge(target):
            cnt = 0
            for left in range(n):
                lo, hi = left, n - 1
                pos = n  # first position with score >= target
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if rmq.score(left, mid) >= target:
                        pos = mid
                        hi = mid - 1
                    else:
                        lo = mid + 1
                if pos < n:
                    cnt += (n - pos)
            return cnt

        # helper: sum of scores strictly greater than target, and their count
        def sum_and_count_gt(target):
            total_sum = 0
            cnt = 0
            for left in range(n):
                lo, hi = left, n - 1
                pos = n  # first position with score > target
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if rmq.score(left, mid) > target:
                        pos = mid
                        hi = mid - 1
                    else:
                        lo = mid + 1
                if pos == n:
                    continue
                # accumulate all subarrays [left, right] with right >= pos
                for right in range(pos, n):
                    val = rmq.score(left, right)
                    if val > target:
                        total_sum += val
                        cnt += 1
                    else:
                        # since score is non-decreasing in right, we can break
                        break
            return total_sum, cnt

        # binary search for target value
        global_min = min(nums)
        global_max = max(nums)
        low, high = 0, global_max - global_min

        while low < high:
            mid = (low + high + 1) // 2
            if count_ge(mid) >= k:
                low = mid
            else:
                high = mid - 1

        target = low
        sum_gt, cnt_gt = sum_and_count_gt(target)
        # remaining subarrays (k - cnt_gt) will have score exactly target
        answer = sum_gt + (k - cnt_gt) * target
        return answer


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
