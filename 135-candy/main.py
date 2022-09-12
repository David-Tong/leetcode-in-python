class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [0] * len(ratings)
        for x in range(len(ratings)):
            if x > 0:
                if ratings[x] > ratings[x - 1]:
                    candies[x] = candies[x - 1] + 1
                else:
                    candies[x] = 1
            else:
                candies[x] = 1
        """
        for x in range(len(ratings), 0, -1):
            if x < len(ratings):
                if ratings[x - 1] > ratings[x]:
                    candies[x - 1] = max(candies[x - 1], candies[x] + 1)
        """
        print(candies)
        return sum(candies)


ratings = [1, 0, 2]
#ratings = [1, 2, 2]
#ratings = [1, 3, 4, 5, 2]

solution = Solution()
print(solution.candy(ratings))
