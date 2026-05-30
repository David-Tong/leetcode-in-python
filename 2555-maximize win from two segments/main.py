class Solution(object):
    def maximizeWin(self, prizePositions, k):
        """
        :type prizePositions: List[int]
        :type k: int
        :rtype: int
        """
        # process
        L = len(prizePositions)

        # search the first sliding window
        # best[x] - the maximum prize number for a valid window on the left of x and x
        left = 0
        best = [0] * L
        for right in range(L):
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
            best[right] = max(best[right - 1] if right > 0 else 0, right - left + 1)

        # search the second sliding window
        # ensure not overlapped with the first sliding window
        ans = 0
        left = 0
        for right in range(L):
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
            first = right - left + 1
            second = best[left - 1] if left > 0 else 0
            ans = max(ans, first + second)

        return ans


prizePositions = [1,1,2,2,3,3,5]
k = 2

solution = Solution()
print(solution.maximizeWin(prizePositions, k))
