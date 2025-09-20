class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(arr)

        # process
        target = L
        ans = list()
        while target > 1:
            # find target
            for x in range(L):
                if arr[x] == target:
                    ans.append(x + 1)
                    # pancake sort
                    arr = arr[:x + 1][::-1] + arr[x + 1:]
                    ans.append(target)
                    # pancake sort again
                    arr = arr[:target][::-1] + arr[target:]
                    break
            target -= 1
        return ans


arr = [3,2,4,1]
arr = [1,2,3]

solution = Solution()
print(solution.pancakeSort(arr))
