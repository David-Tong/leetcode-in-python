class Solution(object):
    def shortestSubstrings(self, arr):
        """
        :type arr: List[str]
        :rtype: List[str]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(set)

        # helper function
        def parse(idx):
            N = len(arr[idx])
            for x in range(N):
                for y in range(x, N):
                    ss = arr[idx][x:y + 1]
                    dicts[ss].add(idx)

        M = len(arr)
        for x in range(M):
            parse(x)
        keys = sorted(dicts.keys(), key=lambda x: (len(x), x))
        # print(keys)
        # print(dicts)

        # process
        ans = [""] * M
        for key in keys:
            if len(dicts[key]) == 1:
                idx = dicts[key].pop()
                if ans[idx] == "":
                    ans[idx] = key
        return ans


arr = ["cab","ad","bad","c"]
arr = ["abc","bcd","abcd"]
arr = ["gfnt","xn","mdz","yfmr","fi","wwncn","hkdy"]
arr = ["vbb","grg","lexn","oklqe","yxav"]

solution = Solution()
print(solution.shortestSubstrings(arr))
