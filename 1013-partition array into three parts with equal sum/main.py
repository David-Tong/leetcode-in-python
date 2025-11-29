class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # pre-process
        L = len(arr)
        from collections import defaultdict
        dicts = defaultdict(list)
        presums = [0]
        for idx, num in enumerate(arr):
            presum = presums[-1] + num
            presums.append(presum)
            dicts[presum].append(idx)
        print(dicts)
        print(presums)

        # process
        from bisect import bisect_right
        for idx in range(L):
            target = presums[idx + 1]
            if target * 2 in dicts:
                idx2 = bisect_right(dicts[target * 2], idx)
                if idx2 < len(dicts[target * 2]) and dicts[target * 2][idx2] < L - 1:
                    if target * 3 == presums[-1]:
                        return True
        return False


arr = [0,2,1,-6,6,-7,9,1,2,0,1]
arr = [0,2,1,-6,6,7,9,-1,2,0,1]
arr = [3,3,6,5,-2,2,5,1,-9,4]
arr = [1,-1,1,-1]
# arr = [0,0,0,0]

solution = Solution()
print(solution.canThreePartsEqualSum(arr))
