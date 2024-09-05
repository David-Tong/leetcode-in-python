class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for num in arr:
            if num % 2 == 1:
                count += 1
            else:
                count = 0
            if count > 2:
                return True
        return False


arr = [2,6,4,1]
arr = [1,2,34,3,4,5,7,23,12]

solution = Solution()
print(solution.threeConsecutiveOdds(arr))
