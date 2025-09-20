class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        # pre-proces
        L = len(fruits)
        placeds = [False] * L

        # process
        ans = 0
        for x in range(L):
            placed = False
            for y in range(L):
                if not placeds[y] and baskets[y] >= fruits[x]:
                    placeds[y] = True
                    placed = True
                    break
            if not placed:
                ans += 1
        return ans


fruits = [4,2,5]
baskets = [3,5,4]

fruits = [3,6,1]
baskets = [6,4,7]

solution = Solution()
print(solution.numOfUnplacedFruits(fruits, baskets))
