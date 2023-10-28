class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        def merge(stones, k):
            key = str(stones) + "-" + str(k)
            if key in self.cache:
                return self.cache[key]

            if len(stones) < k:
                return float("inf")
            elif len(stones) == k:
                return sum(stones)

            ans = float("inf")
            for x in range(len(stones) - k + 1):
                cost = sum(stones[x: x + k])
                ans = min(ans, cost + merge(stones[:x] + [cost] + stones[x + k:], k))

            self.cache[key] = ans
            return ans

        from collections import defaultdict
        self.cache = defaultdict(int)

        ans = merge(stones, k)
        return -1 if ans == float("inf") else ans


stones = [3,2,4,1]
k = 2

stones = [3,2,4,1]
k = 3

stones = [3,5,1,2,6]
k = 3

stones = [3,4,5,6,1,2,3,11,2,1,2,3,45,8,7,1,12,99,12,32]
#stones = [3,4,5,6,1,2,3,11,2,1,2,3,45,8,7,1,12,99,12,32,45,6,7,89,11,2,3,13,14,100]
k = 2

solution = Solution()
print(solution.mergeStones(stones, k))
