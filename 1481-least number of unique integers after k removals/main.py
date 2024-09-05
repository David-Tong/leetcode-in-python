class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        freqs = defaultdict(int)

        for num in arr:
            freqs[num] += 1

        fs = list()
        for freq in freqs:
            fs.append((freqs[freq], freq))
        fs = sorted(fs)

        # process
        idx = 0
        count = k
        while count > 0:
            if count >= fs[idx][0]:
                count -= fs[idx][0]
                idx += 1
            else:
                break

        L = len(fs)
        ans = L - idx
        return ans


arr = [5,5,4]
k = 1

arr = [4,3,1,1,3,3,2]
k = 3

arr = [5,4,5,5,5,5,6,7,8,1,1,1,1,1,1,1,1,1]
k = 10

solution = Solution()
print(solution.findLeastNumOfUniqueInts(arr, k))
