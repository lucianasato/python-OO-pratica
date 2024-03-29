class BankAccount:
    def __init__(self, account_number, name, password, value, admin):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.value = value
        self.admin = admin

    def check_account_number(self, account_number):
        return account_number == self.account_number

    def check_account_password(self, account_password):
        return account_password == self.password

    def balance_debit(self, value):
        self.value -= value

class CashMachineInsertMoneyBill:

    @staticmethod
    def insert_money_bill(money_bill, amount):
        cash_machine = CashMachine({
            '20': 5,
            '50': 5,
            '100': 5,
        })
        cash_machine.money_slips[money_bill] += amount
        return cash_machine

class CashMachineWithDraw:
    @staticmethod
    def withdraw(bank_account, value):
        cash_machine = CashMachine({
            '20': 5,
            '50': 5,
            '100': 5,
        })
        money_slips_user = cash_machine.withdraw(value)
        if money_slips_user:
            bank_account.balance_debit(value)
        return cash_machine

class CashMachine:

    def __init__(self, money_slips):
        self.money_slips = money_slips
        self.money_slips_user = {}
        self.value_remaining = 0

    def withdraw(self, value):
        self.value_remaining = value

        self.__calculate_money_slips_user('100')
        self.__calculate_money_slips_user('50')
        self.__calculate_money_slips_user('20')

        if self.value_remaining == 0:
            self.__decrease_money_slips()

        return False if self.value_remaining != 0 else self.money_slips

    def __calculate_money_slips_user(self, money_bill):
        money_bill_int = int(money_bill)
        if 0 < self.value_remaining // money_bill_int <= self.money_slips[money_bill]:
            self.money_slips_user[money_bill] = self.value_remaining // money_bill_int
            self.value_remaining = self.value_remaining - self.value_remaining // money_bill_int * money_bill_int

    def __decrease_money_slips(self):
        for money_bill in self.money_slips_user:
            self.money_slips[money_bill] -= self.money_slips_user[money_bill]


accounts_list = [
    BankAccount('0001', 'Fulano 1', '123', 100, False),
    BankAccount('0002', 'Fulano 2', '123', 50, False),
    BankAccount('1111', 'Fulano 3', '123', 1000, True),
]