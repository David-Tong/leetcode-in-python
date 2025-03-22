class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        # pre-process
        L = len(ranks)

        # process
        # helper function
        from math import sqrt
        def canRepair(target):
            count = 0
            for rank in ranks:
                count += int(sqrt(target // rank))
            if count >= cars:
                return True
            else:
                return False

        # binary search
        left, right = 1, min(ranks) * cars * cars
        while left + 1 < right:
            middle = (left + right) // 2
            if canRepair(middle):
                right = middle
            else:
                left = middle + 1
        if canRepair(left):
            return left
        else:
            return right


ranks = [4,2,3,1]
cars = 10

ranks = [5,1,8]
cars = 6

ranks = [1,1,23,55]
cars = 10

solution = Solution()
print(solution.repairCars(ranks, cars))
