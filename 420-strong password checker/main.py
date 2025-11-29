class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        # pre-process
        import  string
        need_upper, need_lower, need_number = 1, 1, 1
        for ch in password:
            if ch in string.ascii_lowercase:
                need_lower = 0
            elif ch in string.ascii_uppercase:
                need_upper = 0
            elif ch in string.digits:
                need_number = 0
        missing_types = need_lower + need_upper + need_number

        L = len(password)
        repeats = list()
        count = 1
        for x in range(1, L):
            if password[x] == password[x - 1]:
                count += 1
            else:
                if count >= 3:
                    repeats.append(count)
                count = 1
        if count >= 3:
            repeats.append(count)

        # process
        # case 1 : L < 6
        # insert to meet the condition 1 and 2
        # condition 3 will be met automatically
        if L < 6:
            return max(missing_types, 6 - L)
        # case 2 : 6 <= L <= 20
        # swap, replace aaaaa to aaAaa
        elif 6 <= L <= 20:
            swap_count = 0
            for repeat in repeats:
                swap_count += repeat // 3
            return max(missing_types, swap_count)
        # case 3 : L >= 20
        # delete to have repeating string to be 3k + 2
        # aaaaa is the optimal sub-structure
        else:
            R = len(repeats)
            need_to_remove = L - 20

            # case 3.1
            # delete aaaaaa to aaaaa
            idx = 0
            while idx < R and need_to_remove > 0:
                repeat = repeats[idx]
                if repeat % 3 == 0:
                    need_to_remove -= 1
                    repeats[idx] = repeat - 1
                idx += 1

            # case 3.2
            # delete aaaaaaa to aaaaa
            idx = 0
            while idx < R and need_to_remove > 0:
                repeat = repeats[idx]
                if repeat % 3 == 1 and need_to_remove > 1:
                    need_to_remove -= 2
                    repeats[idx] = repeat - 2
                idx += 1

            # remove the string to be less than 30
            idx = 0
            while idx < R and need_to_remove > 0:
                repeat = repeats[idx]
                while repeat > 3 and need_to_remove >= 3:
                    repeat -= 3
                    need_to_remove -= 3
                repeats[idx] = repeat
                idx += 1

            swap_count = 0
            for repeat in repeats:
                swap_count += repeat // 3
            return max(missing_types, swap_count) + L - 20


password = "a"
password = "aA1"
password = "1337C0d3"
password = "aaa111"

solution = Solution()
print(solution.strongPasswordChecker(password))



