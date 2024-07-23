class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # pre-process
        L = len(arr)

        # process
        ans = 0
        for i in range(L - 1):
            for k in range(i + 1, L):
                left = arr[i]
                right = 0
                for j in range(i + 1, k + 1):
                    right ^= arr[j]
                for j in range(i + 1, k + 1):
                    if j - 1 > i:
                        left ^= arr[j - 1]
                        right ^= arr[j - 1]
                    if left == right:
                        #print(i, j, k)
                        ans += 1
        return ans


arr = [2,3,1,6,7]
arr = [1,1,1,1,1]
arr = [1,1,1,1]

solution = Solution()
print(solution.countTriplets(arr))
