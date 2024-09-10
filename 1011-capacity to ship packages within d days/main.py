class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def canShip(target, weights, days):
            capacity = target
            for weight in weights:
                if target < weight:
                    return False
                if capacity < weight:
                    capacity = target
                    days -= 1
                    if days <= 0:
                        return False
                capacity -= weight
            return True

        left = 1
        right = sum(weights)

        while left + 1 < right:
            middle = (left + right) // 2
            if canShip(middle, weights, days):
                right = middle
            else:
                left = middle + 1

        if canShip(left, weights, days):
            return left
        else:
            return right


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

weights = [3,2,2,4,1,4]
days = 3

weights = [1, 2, 3, 1, 1]
days = 4

weights = [500, 500]
days = 1

solution = Solution()
print(solution.shipWithinDays(weights, days))
