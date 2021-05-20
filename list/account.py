import random


class Account(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def get_info(self):
        code = random.randint(100, 999)
        code1 = random.randint(10, 99)
        code2 = random.randint(100000, 999999)
        print('은행이름: sc은행')
        print(f'계좌번호: {code}-{code1}-{code2}')
        return f'예금주명: {self.name} 잔액: {self.money}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료, 1.입력, 2.출력, 3.삭제, 4.수정')
            if menu == '0':
                print('종료합니다.')
                break
            elif menu == '1':
                ls.append(Account(input('예금주명: '), int(input('잔액: '))))
            elif menu == '2':
                for i in ls:
                    print(i.get_info())
            elif menu == '3':
                del_name = input('삭제할 이름: ')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
            elif menu == '4':
                edit_name = input('수정할 이름: ')
                edit_info = Account(edit_name, int(input('수정할 금액')))
                for i, j in enumerate(ls):
                    if j.name == edit_name:
                        del ls[i]
                        ls.append(edit_info)
            else:
                print('잘못된 입력입니다.')
                continue


Account.main()


