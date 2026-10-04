class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        # pre-process
        from sortedcontainers import SortedList
        L = len(s)
        ranges = {}
        sizes = {}

        # Build initial ranges only for characters that appear
        idx = 0
        while idx < L:
            idx2 = idx
            while idx2 < L and s[idx2] == s[idx]:
                idx2 += 1
            ch = s[idx]

            if ch not in ranges:
                ranges[ch] = SortedList()
                sizes[ch] = SortedList()

            ranges[ch].add((idx, idx2 - 1))
            sizes[ch].add(idx2 - idx)
            idx = idx2

        def remove_from_char(ch, idx):
            lst = ranges[ch]
            pos = lst.bisect_right((idx, float('inf'))) - 1
            if pos < 0 or pos >= len(lst):
                return

            L0, R0 = lst[pos]
            if not (L0 <= idx <= R0):
                return

            lst.remove((L0, R0))
            sizes[ch].remove(R0 - L0 + 1)

            if L0 < idx:
                lst.add((L0, idx - 1))
                sizes[ch].add(idx - L0)
            if idx < R0:
                lst.add((idx + 1, R0))
                sizes[ch].add(R0 - idx)

            if len(lst) == 0:
                del ranges[ch]
                del sizes[ch]

        def add_to_char(ch, idx):
            if ch not in ranges:
                ranges[ch] = SortedList()
                sizes[ch] = SortedList()

            lst = ranges[ch]
            pos = lst.bisect_left((idx, idx))

            left_merge = None
            right_merge = None

            if pos > 0:
                L0, R0 = lst[pos - 1]
                if R0 + 1 == idx:
                    left_merge = (L0, R0)

            if pos < len(lst):
                L1, R1 = lst[pos]
                if L1 - 1 == idx:
                    right_merge = (L1, R1)

            if left_merge and right_merge:
                lst.remove(left_merge)
                lst.remove(right_merge)
                sizes[ch].remove(left_merge[1] - left_merge[0] + 1)
                sizes[ch].remove(right_merge[1] - right_merge[0] + 1)

                new_range = (left_merge[0], right_merge[1])
                lst.add(new_range)
                sizes[ch].add(new_range[1] - new_range[0] + 1)

            elif left_merge:
                lst.remove(left_merge)
                sizes[ch].remove(left_merge[1] - left_merge[0] + 1)

                new_range = (left_merge[0], idx)
                lst.add(new_range)
                sizes[ch].add(new_range[1] - new_range[0] + 1)

            elif right_merge:
                lst.remove(right_merge)
                sizes[ch].remove(right_merge[1] - right_merge[0] + 1)

                new_range = (idx, right_merge[1])
                lst.add(new_range)
                sizes[ch].add(new_range[1] - new_range[0] + 1)

            else:
                lst.add((idx, idx))
                sizes[ch].add(1)

        s = list(s)
        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            old = s[idx]
            if old != ch:
                remove_from_char(old, idx)
                add_to_char(ch, idx)
                s[idx] = ch

            best = 1
            for ch in sizes:
                if len(sizes[ch]) > 0:
                    best = max(best, sizes[ch][-1])
            ans.append(best)
        return ans


s = "babacc"
queryCharacters = "bcb"
queryIndices = [1,3,3]

s = "abyzz"
queryCharacters = "aa"
queryIndices = [2,1]

s = "mqvivodnwlqkblnacpvqkonwaemvglhkkhcpxohmntoqhyeyvvjowcdhodujtujjooeddxvjfhpppgiw"
queryCharacters = "owwjnooweqoutilhpnajyjiaqvxcokqpeziczagypahzssiweedeot"
queryIndices = [29,21,0,2,21,61,0,63,9,9,60,13,68,16,57,42,69,26,32,28,73,8,51,29,33,2,44,53,7,19,21,1,0,73,19,53,50,65,31,21,65,29,19,73,18,31,12,34,77,44,22,11,44,21]

solution = Solution()
print(solution.longestRepeating(s, queryCharacters, queryIndices))
