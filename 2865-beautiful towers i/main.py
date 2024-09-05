class Solution(object):
    def maximumSumOfHeights(self, maxHeights):
        """
        :type maxHeights: List[int]
        :rtype: int
        """
        # pre-process
        L = len(maxHeights)

        # process
        ans = 0
        for idx in range(L):
            total = maxHeights[idx]
            # search left
            left = idx - 1
            prev = maxHeights[idx]
            while left >= 0:
                if maxHeights[left] > prev:
                    total += prev
                else:
                    total += maxHeights[left]
                    prev= maxHeights[left]
                left -= 1
            # search right
            right = idx + 1
            prev = maxHeights[idx]
            while right < L:
                if maxHeights[right] > prev:
                    total += prev
                else:
                    total += maxHeights[right]
                    prev = maxHeights[right]
                right += 1
            ans = max(ans, total)
        return ans


maxHeights = [5,3,4,1,1]
maxHeights = [6,5,3,9,2,7]
maxHeights = [3,2,5,5,2,3]
maxHeights = [3,2,5,3,5,2,3]
maxHeights = [3,2,5,3,4,5,2,3]
maxHeights = [5,2,4,4]

solution = Solution()
print(solution.maximumSumOfHeights(maxHeights))
