class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        N = len(nums)
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, num in enumerate(nums):
            dicts[num].append(idx)

        # process
        # helper
        def equal(group, idx):
            for x in range(len(group)):
                if idx + x >= N:
                    return False
                if group[x] != nums[idx + x]:
                    return False
            return True

        idx = 0
        for group in groups:
            first = group[0]
            match = False
            for nidx in dicts[first]:
                if nidx >= idx:
                    idx = nidx
                    if equal(group, idx):
                        idx += len(group)
                        match = True
                        break
            if not match:
                return False
        return True


groups = [[1,-1,-1],[3,-2,0]]
nums = [1,-1,0,1,-1,-1,3,-2,0]

groups = [[10,-2],[1,2,3,4]]
nums = [1,2,3,4,10,-2]

groups = [[1,2,3],[3,4]]
nums = [7,7,1,2,3,4,7,7]

groups = [[1,2,3],[3,4]]
nums = [7,7,1,2,3,3,5,4,7,7]

groups =[[2,1]]
nums = [12,1]

groups = [[1,2,3],[3,4]]
nums = [1,2,3,3,4]

solution = Solution()
print(solution.canChoose(groups, nums))
