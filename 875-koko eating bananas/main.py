class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def canEat(speed, piles, h):
            for pile in piles:
                if pile % speed == 0:
                    h -= pile // speed
                else:
                    h -= (pile // speed) + 1
                if h < 0:
                    return False
            return True

        left = 1
        right = max(piles)

        while left + 1 < right:
            middle = (left + right) // 2
            if canEat(middle, piles, h):
                right = middle
            else:
                left = middle + 1

        if canEat(left, piles, h):
            return left
        else:
            return right


piles = [3,6,7,11]
h = 8

piles = [30,11,23,4,20]
h = 5

piles = [30,11,23,4,20]
h = 6

solution = Solution()
print(solution.minEatingSpeed(piles, h))
