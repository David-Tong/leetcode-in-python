class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # pre-process
        # helper function
        # convert to binary array
        def convert(num):
            res = list()
            while num:
                res.append(num & 1)
                num >>= 1
            return res

        arr = convert(n)
        arr2 = convert(k)
        M, N = len(arr), len(arr2)

        # process
        if M < N:
            return -1
        ans = 0
        idx = 0
        while idx < N:
            if arr[idx] == 0:
                if arr2[idx] == 1:
                    return -1
            elif arr[idx] == 1:
                if arr2[idx] == 0:
                    ans += 1
            idx += 1
        while idx < M:
            if arr[idx] == 1:
                ans += 1
            idx += 1
        return ans


n = 13
k = 4

"""
n = 21
k = 21

n = 14
k = 13
"""

solution = Solution()
print(solution.minChanges(n, k))