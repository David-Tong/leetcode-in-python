class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        L = len(arr)

        # rule one used when one is True, otherwise false
        one = True
        ans = 1
        for x in range(L - 1):
            if x == 0:
                if arr[x] < arr[x + 1]:
                    one = True
                    size = 2
                elif arr[x] > arr[x + 1]:
                    one = False
                    size = 2
                else:
                    one = False
                    size = 1
            else:
                if x % 2 == 0:
                    if arr[x] < arr[x + 1]:
                        if one:
                            size += 1
                        else:
                            size = 2
                            one = True
                    elif arr[x] > arr[x + 1]:
                        if one:
                            size = 2
                            one = False
                        else:
                            size += 1
                            one = False
                    else:
                        size = 2
                else:
                    if arr[x] > arr[x + 1]:
                        if one:
                            size += 1
                        else:
                            size = 2
                            one = True
                    elif arr[x] < arr[x + 1]:
                        if one:
                            size = 2
                            one = False
                        else:
                            size += 1
                            one = False
                    else:
                        size = 1
            ans = max(ans, size)
        return ans


arr = [9,4,2,10,7,8,8,1,9]
arr = [4,8,12,16]
arr = [100]
arr = [1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,2,1,2]
arr = [9,9]
arr = [100, 100, 100]

solution = Solution()
print(solution.maxTurbulenceSize(arr))
