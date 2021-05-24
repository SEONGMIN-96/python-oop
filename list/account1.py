class Account(object):
    def __init__(self, account_number, name, money):
        self.BANK_NAME = 'SC은행'
        self.account_number = account_number
        self.name = name
        self.money = money

    def to_string(self):
        return self.BANK_NAME, self.account_number, self.name, self.money

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0. exit 1. create 2. read 3. update 4. delete')
            if menu == '0':
                ls.append(Account(i.account_number, input('name'), input('money')))
            elif menu == '1':
                for i in ls:
                    print(i.to_string())
            elif menu == '2':
                account_number = input('account_number')
                money = input('입금할 금액')
                for i, j in enumerate(ls):
                    if j == account_number:
                        del [i]









Account.main()