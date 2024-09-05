class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # pre-process
        L = len(arr)

        from collections import defaultdict
        cache = defaultdict(int)

        dicts = defaultdict(int)
        for idx, item in enumerate(arr):
            dicts[item] = idx

        # process
        for x in range(L):
            for y in range(x + 1, L):
                stack = list()
                l = 1
                if arr[x] + arr[y] in dicts:
                    stack.append(arr[x])
                    stack.append(arr[y])
                    while stack[-1] + stack[-2] in dicts:
                        key = str(stack[-2]) + "-" + str(stack[-1])
                        if key in cache:
                            l = cache[key]
                            break
                        else:
                            stack.append(stack[-1] + stack[-2])
                while len(stack) > 1:
                    key = str(stack[-2]) + "-" + str(stack[-1])
                    stack.pop()
                    cache[key] = l
                    l += 1

        ans = max(cache.values()) + 1 if cache.values() else 0
        return ans


arr = [1,2,3,4,5,6,7,8]
arr = [1,3,7,11,12,14,18]
arr = [1,2,3,4,5,6,8,9,10,11,12,13,25,26,28,38]
arr = [1,3,5]

solution = Solution()
print(solution.lenLongestFibSubseq(arr))
