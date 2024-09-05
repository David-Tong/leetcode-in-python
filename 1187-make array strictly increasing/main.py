class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # pre-process arr2
        arr2 = sorted(list(set(arr2)))

        M = len(arr1)
        N = len(arr2)

        # dp
        # keep[x] - the minimal cost to keep xth element in arr1 to make arr1 legal
        keep = [float("inf")] * M
        keep[0] = 0

        # swap[x][y] - the minimal cost to swap xth element in arr1 to yth element in arr2
        #              to make arr1 legal
        swap = [[float("inf")] * N for _ in range(M)]
        for y in range(N):
            swap[0][y] = 1

        for x in range(M):
            mini_keep = float("inf")
            mini_swap = float("inf")
            if arr1[x] > arr1[x - 1]:
                keep[x] = keep[x - 1]

            for y in range(N):
                if y > 0:
                    mini_swap = min(mini_swap, swap[x - 1][y - 1] + 1)
                if arr1[x] > arr2[y]:
                    mini_keep = min(mini_keep, swap[x - 1][y])
                if arr2[y] > arr1[x - 1]:
                    swap[x][y] = keep[x - 1] + 1

                swap[x][y] = min(swap[x][y], mini_swap)
                keep[x] = min(keep[x], mini_keep)

        ans = min(keep[M - 1], min(swap[M - 1]))
        return -1 if ans == float("inf") else ans


arr1 = [1,5,3,6,7]
arr2 = [1,3,2,4]

arr1 = [1,5,3,6,7]
arr2 = [4,3,1]

arr1 = [1,5,3,6,7]
arr2 = [1,6,3,3]

arr1 = [1,3,5,2,3,4,5,6,7,8]
arr2 = [2,3,4,1,2,2]

arr1 = [0,11,6,1,4,3]
arr2 = [5,4,11,10,1,0]

arr1 = [5,16,19,2,1,12,7,14,5,16]
arr2 = [6,17,4,3,6,13,4,3,18,17,16,7,14,1,16]

solution = Solution()
print(solution.makeArrayIncreasing(arr1, arr2))
