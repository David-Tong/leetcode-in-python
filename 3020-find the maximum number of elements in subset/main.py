class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1

        ones, twos = defaultdict(bool), defaultdict(bool)
        for num in dicts:
            if dicts[num] == 1:
                ones[num] = False
            else:
                ones[num] = False
                twos[num] = False
        # print(ones)
        # print(twos)

        # process
        # conner case
        if 1 in dicts:
            one = dicts[1]
            ans = one - 1 if one % 2 == 0 else one
        else:
            ans = 1

        for two in sorted(twos):
            if two != 1:
                seq = 0
                while two in twos and not twos[two]:
                    seq += 1
                    twos[two] = True
                    two = two ** 2
                    if two not in twos:
                        if two in ones:
                            ans = max(ans, seq * 2 + 1)
                            break
                    else:
                        ans = max(ans, seq * 2 + 1)
        return ans


nums = [5,4,1,2,2]
nums = [1,3,2,4]
nums = [2,2,4,4,8,16,256,16]
nums = [2,2,4,4,8,16,64,16]
nums = [1,1]
nums = [2,4,6]

solution = Solution()
print(solution.maximumLength(nums))
