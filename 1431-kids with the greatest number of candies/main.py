class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        greatest = max(candies)

        ans = list()
        for candy in candies:
            if candy + extraCandies >= greatest:
                ans.append(True)
            else:
                ans.append(False)
        return ans


candies = [2,3,5,1,3]
extraCandies = 3

candies = [4,2,1,1,2]
extraCandies = 1

candies = [12,1,12]
extraCandies = 10

solution = Solution()
print(solution.kidsWithCandies(candies, extraCandies))
