class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_info(self):
        return f'종목명: {self.name}, 종목코드: {self.code}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = (input('0.종료 1.입력 2.출력 3.삭제 4.수정'))
            if menu == '0':
                print('종료합니다.')
                break
            elif menu == '1':
                ls.append(Stock(input('종목명: '), int(input('종목코드: '))))
            elif menu == '2':
                for i in ls:
                    print(i.get_info())
            elif menu == '3':
                del_name = input('삭제할 이름: ')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
            else:
                print('잘못된 입력입니다.')
                continue


Stock.main()
