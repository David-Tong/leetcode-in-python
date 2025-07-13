class Solution(object):
    def maxDifference(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def replace(ch, ch2):
            nums = list()
            for c in s:
                if c == ch:
                    nums.append(1)
                elif c == ch2:
                    nums.append(-1)
                else:
                    nums.append(0)
            return nums

        def opposite(state):
            if state == "00":
                return "10"
            elif state == "01":
                return "11"
            elif state == "10":
                return "00"
            elif state == "11":
                return "01"

        # nums - after a replaced to 1 and b replaced to -1, others to 0
        #      - a has a frequency of odd and b has a frequency of even
        def count(nums):
            # pre-process
            presums = list()
            presums.append(0)

            from collections import defaultdict
            states = defaultdict(list)
            # state - 00 means both a and b are even
            #       - 01 means a is even and b is odd
            #       - 10 means a is odd and b is even
            #       - 11 means a is odd and b is odd
            STATES = ["00", "01", "10", "11"]
            for state in STATES:
                if state == "00":
                    states[state].append(0)
                else:
                    states[state].append(float("inf"))
            chs, chs2 = 0, 0

            # process
            ans = float("-inf")
            for idx, num in enumerate(nums):
                if num == 1:
                    chs += 1
                elif num == -1:
                    chs2 += 1
                mod, mod2 = chs % 2, chs2 % 2
                state = "{}{}".format(str(mod), str(mod2))
                presum = presums[-1] + num
                presums.append(presum)

                # update state
                for ste in STATES:
                    if ste == state and chs > 0 and chs2 > 0:
                        states[ste].append(min(states[ste][-1], presum))
                    else:
                        states[ste].append(states[ste][-1])

                # calculate
                opposite_state = opposite(state)
                if idx >= k - 1:
                    print(idx, presum, states[opposite_state][idx - k + 1], presum - states[opposite_state][idx - k + 1])
                    ans = max(ans, presum - states[opposite_state][idx - k + 1])
            return ans

        # pre-process
        digits = set()
        for c in s:
            digits.add(c)

        # process
        ans = float("-inf")
        for ch in digits:
            for ch2 in digits:
                if ch != ch2:
                    print(ch, ch2)
                    nums = replace(ch, ch2)
                    print(nums)
                    cnt = count(nums)
                    print(cnt)
                    ans = max(ans, cnt)
        return ans


s = "12233"
k = 4

s = "1122211"
k = 3

solution = Solution()
print(solution.maxDifference(s, k))
