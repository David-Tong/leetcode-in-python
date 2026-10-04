class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        # pre-process
        # process s part
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s:
            dicts[ch] += 1
        keys = sorted(dicts.keys())
        K = len(keys)

        # check palindromic condition
        odds = 0
        odd_char = None
        for key in keys:
            if dicts[key] % 2 == 1:
                odds += 1
                odd_char = key
            dicts[key] //= 2
        if odds > 1:
            return ""

        # process target psrt
        L = len(target)
        H = L // 2
        target_half = target[: H]

        # helper function
        # find the existing character greater than ch
        def advance(ch):
            idx = 0
            while idx < K:
                key = keys[idx]
                if key > ch:
                    if dicts[key] > 0:
                        return key
                idx += 1
            return None

        # make the string in a lexicographically smallest way'
        def compose(idx, advanced):
            # build the first half
            first = target_half[:idx] + advanced

            # use remaining dicts to fill the rest of first half
            remain = []
            for key in keys:
                if dicts[key] > 0:
                    remain.append(key * dicts[key])
            remain = "".join(remain)
            first += remain

            # now build palindrome
            if odd_char is None:
                return first + first[::-1]
            else:
                return first + odd_char + first[::-1]

        # process
        # within the palindromic radius, map s to target exactly, as much as possible
        idx = 0
        while idx < H and dicts[target[idx]] > 0:
            dicts[target[idx]] -= 1
            idx += 1

        # reach the rightest position, within the palindromic radius, where s can map to target exactly
        # use a generic algorithm, no matter if s contains same characters as target

        # step 1: reach the rightest matches position
        # check if reach the end
        if idx < H:
            ch = target_half[idx]
            advanced = advance(ch)
            if advanced is not None:
                dicts[advanced] -= 1
                return compose(idx, advanced)
        else:
            composed = compose(idx, "")
            if composed > target:
                return composed
        idx -= 1

        # step 2 : traceback to find the next greater string
        while idx >= 0:
            ch = target_half[idx]
            advanced = advance(ch)
            if advanced is not None:
                dicts[ch] += 1
                dicts[advanced] -= 1
                return compose(idx, advanced)
            ch2 = target[idx]
            dicts[ch2] += 1
            idx -= 1
        return ""


s = "baba"
target = "abba"

s = "baba"
target = "bbaa"

s = "abc"
target = "abb"

s = "aac"
target = "abb"

s = "abcab"
target = "abcab"

s = "aabbcc"
target = "abccaa"

s = "aab"
target = "aaa"

s = "aabb"
target = "aaaa"

s = "aaabb"
target = "ababa"

s = "aabbcc"
target = "aabbaa"

solution = Solution()
print(solution.lexPalindromicPermutation(s, target))
