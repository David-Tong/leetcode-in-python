class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        # pre-process
        L = len(arr)
        target = sorted(target)
        arr = sorted(arr)

        # process
        for x in range(L):
            if target[x] != arr[x]:
                return False
        return True


target = [1,2,3,4]
arr = [2,4,1,3]

target = [7]
arr = [7]

target = [3,7,9]
arr = [3,7,11]

solution = Solution()
print(solution.canBeEqual(target, arr))
