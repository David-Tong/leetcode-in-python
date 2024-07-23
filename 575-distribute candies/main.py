class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        L = len(candyType)
        candyT = set()
        for candyTp in candyType:
            candyT.add(candyTp)
        return min(L // 2, len(candyT))


candyType = [1,1,2,2,3,3]
candyType = [1,1,2,3]
candyType = [6,6,6,6]

solution = Solution()
print(solution.distributeCandies(candyType))
