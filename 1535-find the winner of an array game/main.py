class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        L = len(arr)

        idx = 0
        idx2 = 1

        count = 0
        while idx2 < L:
            if arr[idx] > arr[idx2]:
                idx2 += 1
                count += 1
            else:
                idx = idx2
                idx2 += 1
                count = 1
            if count == k:
                return arr[idx]
        return arr[idx]


arr = [2,1,3,5,4,6,7]
k = 2

arr = [3,2,1]
k = 10

arr = [2,3,4,5,1,7,8,9,11,12,34,6,16]
k = 10

arr = [1,25,35,42,68,70]
k = 1

arr = [2,3]
k = 1

solution = Solution()
print(solution.getWinner(arr, k))
