class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        def is_valid(houses, heaters, radius):
            curr_house = 0
            curr_heater = 0
            n = len(houses)
            m = len(heaters)

            while curr_house < n and curr_heater < m:
                while curr_heater != m and abs(heaters[curr_heater] - houses[curr_house]) > radius:
                    curr_heater += 1
                if curr_heater == m:
                    return False
                curr_house += 1
            return True

        houses = sorted(houses)
        heaters = sorted(heaters)

        left = 0
        right = 10e9
        while left + 1 < right:
            middle = int((left + right) // 2)
            if is_valid(houses, heaters, middle):
                right = middle
            else:
                left = middle

        if is_valid(houses, heaters, left):
            return left
        else:
            return right


houses = [1, 2, 3]
heaters = [2]

houses = [1, 2, 3, 4]
heaters = [1, 4]

houses = [1, 5]
heaters = [2]

houses = [282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923]
heaters = [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 41282327, 16531729, 823378840, 143542612]

solution = Solution()
print(solution.findRadius(houses, heaters))
