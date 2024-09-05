class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        excluded = list()
        for num1 in arr1:
            dicts[num1] += 1
            if num1 not in arr2:
                excluded.append(num1)
        excluded = sorted(excluded)

        # process
        ans = list()
        for num2 in arr2:
            add = [num2] * dicts[num2]
            ans.extend(add)
        ans.extend(excluded)
        return ans


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]

solution = Solution()
print(solution.relativeSortArray(arr1, arr2))
