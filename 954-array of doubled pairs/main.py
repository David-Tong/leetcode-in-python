class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import defaultdict
        N = len(arr)
        dicts = defaultdict(int)
        for item in arr:
            dicts[item] += 1

        count = 0
        arr = sorted(arr)
        for idx, item in enumerate(arr):
            if item in dicts and dicts[item] > 0:
                double = arr[idx] * 2
                if double in dicts and dicts[double] > 0:
                    if double == 0:
                        if dicts[double] > 1:
                            dicts[double] -= 2
                            count += 2
                    else:
                        dicts[double] -= 1
                        dicts[item] -= 1
                        count += 2
        if count == N:
            return True
        else:
            return False


arr = [3, 1, 3, 6]
arr = [2, 1, 2, 6]
arr = [1, 2, 2, 1, 0, 0, 3, 7]
#arr = [4, -2, 2, -4]
arr = [-33, 0]
arr = [-33, 0, 0, 0]

solution = Solution()
print(solution.canReorderDoubled(arr))
