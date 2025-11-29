class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        self.L = len(balance)

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if account1 > self.L or account2 > self.L:
            return False
        if self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        else:
            return False

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account > self.L:
            return False
        else:
            self.balance[account - 1] += money
            return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account > self.L:
            return False

        if self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        else:
            return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
"""
bnk = Bank([10, 100, 20, 50, 30])
print(bnk.withdraw(3, 10))
print(bnk.transfer(5, 1, 20))
print(bnk.deposit(5, 20))
print(bnk.transfer(3, 4, 15))
print(bnk.withdraw(10, 50))
"""

bnk = Bank([767,653,252,849,480,187,761,243,408,385,334,732,289,886,149,320,827,111,315,155,695,110,473,585,83,936,188,818,33,984,66,549,954,761,662,212,208,215,251,792,956,261,863,374,411,639,599,418,909,208,984,602,741,302,911,616,537,422,61,746,206,396,446,661,48,156,725,662,422,624,704,143,94,702,126,76,539,83,270,717,736,393,607,895,661])
print(bnk.deposit(68,668))
print(bnk.deposit(25,978))
print(bnk.transfer(8,31,924))
print(bnk.transfer(2,6,857))
print(bnk.transfer(20,43,59))
print(bnk.deposit(71,307))
print(bnk.transfer(11,46,577))
print(bnk.withdraw(37,377))
print(bnk.deposit(72,835))
print(bnk.withdraw(82,574))
print(bnk.transfer(67,9,939))
print(bnk.transfer(24,49,251))
