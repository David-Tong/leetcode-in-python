class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        items = set(arr)

        zeros = 0
        for item in arr:
            if item == 0:
                zeros += 1
            else:
                if 2 * item in items:
                    return True

        if zeros > 1:
            return True
        else:
            return False


arr = [10,2,5,3]
arr = [7,1,14,11]
arr = [3,1,7,11]
arr = [-2,0,10,-19,4,6,-8]

solution = Solution()
print(solution.checkIfExist(arr))
