class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        box_types = sorted(boxTypes, key=lambda x: -1 * x[1])
        box_size = 0
        ans = 0
        for numbers, units in box_types:
            if box_size + numbers <= truckSize:
                box_size += numbers
                ans += units * numbers
            else:
                ans += units * (truckSize - box_size)
                break
        return ans


boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10

boxTypes = [[10, 10]]
truckSize = 5

solution = Solution()
print(solution.maximumUnits(boxTypes, truckSize))
