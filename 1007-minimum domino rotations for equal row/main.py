class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        from collections import Counter
        L = len(tops)
        top_counter = Counter(tops)
        bottom_counter = Counter(bottoms)

        target = -1
        for num in top_counter:
            if top_counter[num] + bottom_counter[num] >= L:
                target = num
                break

        if target == -1:
            return -1

        if top_counter[target] > bottom_counter[target]:
            to_rotate = bottoms
            rotate_to = tops
        else:
            to_rotate = tops
            rotate_to = bottoms

        for x in range(L):
            if rotate_to[x] != target:
                if to_rotate[x] != target:
                    return -1

        return L - max(top_counter[target], bottom_counter[target])


tops = [2, 1, 2, 4, 2, 2]
bottoms = [5, 2, 6, 2, 3, 2]

tops = [3, 5, 1, 2, 3]
bottoms = [3, 6, 3, 3, 4]

tops = [3, 3, 2, 1]
bottoms = [1, 2, 3, 3]

solution = Solution()
print(solution.minDominoRotations(tops, bottoms))
