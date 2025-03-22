class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        # pre-process
        L = len(pattern)
        nums = [x + 1 for x in range(L + 1)]

        # process
        # validate function
        def validate(sequence):
            for x in range(L):
                if pattern[x] == "I":
                    if sequence[x] >= sequence[x + 1]:
                        return False
                elif pattern[x] == "D":
                    if sequence[x] <= sequence[x + 1]:
                        return False
            return True

        from itertools import permutations
        sequences = permutations(nums)

        ans = ""
        for sequence in sequences:
            if validate(sequence):
                ans = "".join([str(x) for x in sequence])
                return ans


pattern = "IIIDIDDD"
# pattern = "DDD"

solution = Solution()
print(solution.smallestNumber(pattern))