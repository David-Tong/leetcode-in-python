class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        N = len(piles)

        def take(left, right):
            key = str(left) + "-" + str(right)
            if key in self.cache:
                return self.cache[key]

            if left > right:
                return 0

            min_max = float("inf")
            min_max = max(min_max, piles[left] - take(left + 1, right))
            min_max = max(min_max, piles[right] - take(left, right - 1))

            self.cache[key] = min_max
            return min_max

        from collections import defaultdict
        self.cache = defaultdict(int)

        if take(0, N - 1) > 0:
            return True
        else:
            return False


piles = [5,3,4,5]
piles = [3,7,2,3]
piles = [10,22,56,12,3,4,6,18,109,21,56]

solution = Solution()
print(solution.stoneGame(piles))
