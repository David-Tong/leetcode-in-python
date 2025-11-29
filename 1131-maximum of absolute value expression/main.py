class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # pre-process
        L = len(arr1)

        from sortedcontainers import SortedList
        sorted_list = [SortedList() for _ in range(2 ** 3)]
        for x in range(L):
            sorted_list[0].add(arr1[x] + arr2[x] + x)
            sorted_list[1].add(arr1[x] + arr2[x] - x)
            sorted_list[2].add(arr1[x] - arr2[x] + x)
            sorted_list[3].add(arr1[x] - arr2[x] - x)
            sorted_list[4].add(-arr1[x] + arr2[x] + x)
            sorted_list[5].add(-arr1[x] + arr2[x] - x)
            sorted_list[6].add(-arr1[x] - arr2[x] + x)
            sorted_list[7].add(-arr1[x] - arr2[x] - x)

        # process
        ans = max(sorted_list[0][-1] - sorted_list[0][0],
            max(sorted_list[1][-1] - sorted_list[1][0],
                max(sorted_list[2][-1] - sorted_list[2][0],
                    max(sorted_list[3][-1] - sorted_list[3][0],
                        max(sorted_list[4][-1] - sorted_list[4][0],
                            max(sorted_list[5][-1] - sorted_list[5][0],
                                max(sorted_list[6][-1] - sorted_list[6][0],
                                    sorted_list[7][-1] - sorted_list[7][0])
                            )
                        )
                    )
                )
            )
        )

        return ans


arr1 = [1,2,3,4]
arr2 = [-1,4,5,6]

arr1 = [1,-2,-5,0,10]
arr2 = [0,-2,-1,-7,-4]

solution = Solution()
print(solution.maxAbsValExpr(arr1, arr2))
