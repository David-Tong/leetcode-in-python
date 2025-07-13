class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        # pre-process
        L = len(plants)

        # process
        ans = 0
        c = capacity
        for x in range(L):
            if c < plants[x]:
                ans += 2 * x
                c = capacity
            c -= plants[x]
            ans += 1
        return ans


plants = [2,2,3,3]
capacity = 5

plants = [1,1,1,4,2,3]
capacity = 4

plants = [7,7,7,7,7,7,7]
capacity = 8

solution = Solution()
print(solution.wateringPlants(plants, capacity))
