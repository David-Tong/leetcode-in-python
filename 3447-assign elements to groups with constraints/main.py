class Solution(object):
    def assignElements(self, groups, elements):
        """
        :type groups: List[int]
        :type elements: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = max(groups)
        assignments = [-1] * (L + 1)
        for idx, element in enumerate(elements):
            if element <= L:
                if assignments[element] != -1:
                    continue
                for fold in range(element, L + 1, element):
                    if assignments[fold] == -1:
                        assignments[fold] = idx

        # print(assignments)
        ans = [assignments[x] for x in groups]
        return ans


groups = [8,4,3,2,4]
elements = [4,2]

groups = [2,3,5,7]
elements = [5,3,3]

groups = [10,21,30,41]
elements = [2, 1]

groups = [1]
elements = [7]

solution = Solution()
print(solution.assignElements(groups, elements))
