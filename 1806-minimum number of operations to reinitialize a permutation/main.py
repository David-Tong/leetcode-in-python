class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        # helper function
        # operate
        def operate(arr):
            res = [0] * n
            idx = 0
            while idx < n:
                if idx % 2 == 0:
                    res[idx] = arr[idx // 2]
                else:
                    res[idx] = arr[n // 2 + (idx - 1) // 2]
                idx += 1
            return res

        # validate
        def validate(arr):
            idx = 0
            while idx < n:
                if arr[idx] != idx:
                    return False
                idx += 1
            return True

        # process
        arr = [_ for _ in range(n)]
        arr = operate(arr)
        # print(arr)
        ans = 1
        while not validate(arr):
            arr = operate(arr)
            # print(arr)
            ans += 1
        return ans


n = 2
n = 4
n = 6

solution = Solution()
print(solution.reinitializePermutation(n))
