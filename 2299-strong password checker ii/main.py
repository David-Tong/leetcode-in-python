class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        if len(password) < 8:
            return False

        has_lowercase = False
        has_uppercase = False
        has_digit = False
        has_special_character = False

        for idx, char in enumerate(password):
            if ord('a') <= ord(char) <= ord('z'):
                has_lowercase = True
            elif ord('A') <= ord(char) <= ord('Z'):
                has_uppercase = True
            elif ord('0') <= ord(char) <= ord('9'):
                has_digit = True
            elif char in "!@#$%^&*()-+":
                has_special_character = True

            if idx > 0:
                if password[idx] == password[idx - 1]:
                    return  False

        return has_lowercase & has_uppercase & has_digit & has_special_character


password = "IloveLe3tcode!"
password = "Me+You--IsMyDream"
password = "1aB!"
password = "Passw0rd"
password = "Pasw0rd!"
password = "ziyS5FrPQhoQ5oEWRpHW2MjI7sGfcMJdcsjQnIyRbdCilvFaQN07jQtAkOklbjFrU5KcHzw4EvJ41Yz2Ykyd"

solution = Solution()
print(solution.strongPasswordCheckerII(password))
