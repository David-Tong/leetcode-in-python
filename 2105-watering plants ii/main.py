class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        # pre-process
        L = len(plants)

        # process
        alices, bobs = capacityA, capacityB
        left, right = 0, L - 1
        ans = 0
        while left <= right:
            if left < right:
                if plants[left] > alices:
                    alices = capacityA
                    ans += 1
                alices -= plants[left]

                if plants[right] > bobs:
                    bobs = capacityB
                    ans += 1
                bobs -= plants[right]
            elif left == right:
                if bobs > alices:
                    if plants[left] > bobs:
                        bobs = capacityB
                        ans += 1
                    bobs -= plants[left]
                else:
                    if plants[left] > alices:
                        alices = capacityA
                        ans += 1
                    alices -= plants[left]
            left += 1
            right -= 1

        return ans


plants = [2,2,3,3]
capacityA = 5
capacityB = 5

plants = [2,2,3,3]
capacityA = 3
capacityB = 4

plants = [5]
capacityA = 10
capacityB = 8

plants = [2,2,3,3,3]
capacityA = 3
capacityB = 4

solution = Solution()
print(solution.minimumRefill(plants, capacityA, capacityB))
