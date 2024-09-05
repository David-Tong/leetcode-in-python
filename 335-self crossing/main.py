class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        L = len(distance)

        if L <= 3:
            return False

        for x in range(3, L):
            if x >= 3:
                if distance[x] >= distance[x - 2] and distance[x - 1] <= distance[x - 3]:
                    return True
            if x >= 4:
                if distance[x - 1] == distance[x - 3] and distance[x] + distance[x - 4] >= distance[x - 2]:
                    return True
            if x >= 5:
                if distance[x - 2] >= distance[x - 4] and distance[x - 5] + distance[x - 1] >= distance[x - 3] and distance[x - 1] <= distance[x - 3] and distance[x - 4] + distance[x] >= distance[x - 2]:
                    return True
        return False


distance = [2,1,1,2]
distance = [1,2,3,4]
distance = [1,1,1,2,1]
distance = [2,3,4,5,2,1,1]
distance = [2,3,4,5,2,2,1]
distance = [2,3,5,5,2,4,1,4]
distance = [3,3,4,2,2]
distance = [3,3,2,1,1]
distance = [3,3,3,2,1,1]

solution = Solution()
print(solution.isSelfCrossing(distance))
