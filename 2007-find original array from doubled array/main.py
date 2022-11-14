class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        dicts = defaultdict(int)

        for num in changed:
            dicts[num] += 1

        changed = sorted(changed)

        ans = list()
        for num in changed:
            if dicts[num] > 0:
                double = num * 2
                if double in dicts and dicts[double] > 0:
                    dicts[num] -= 1
                    dicts[double] -= 1
                    if dicts[num] >= 0 and dicts[double] >= 0:
                        ans.append(num)
                    else:
                        return list()
                else:
                    return list()

        return ans


changed = [1,3,4,2,6,8]
changed = [6,3,0,1]
changed = [6,3,0,0]
changed = [1]
changed = [0]

solution = Solution()
print(solution.findOriginalArray(changed))
