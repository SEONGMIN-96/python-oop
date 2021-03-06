"""
이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
"""


class Contacts(object):
    def __init__(self, name, number, email, address):
        self.name = name
        self.number = number
        self.email = email
        self.address = address

    def get_info(self):
        return f'입력정보 이름: {self.name} 전화번호: {self.number} 이메일: {self.email} 주소: {self.address}'

    @staticmethod
    def del_element(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = (input('0.종료 1.입력 2.출력 3.삭제 4.수정'))
            if menu == '1':
                ls.append(Contacts(input('성함'), int(input('전화번호')), input('이메일'), input('주소')))
            elif menu == '2':
                for i in ls:
                    print(f'출력결과: {i.get_info()}')
            elif menu == '0':
                print('종료합니다.')
                break
            elif menu == '3':
                name = input('삭제할 이름: ')
                Contacts.del_element(ls, name)

            elif menu == '4':
                edit_name = input('수정할 이름: ')
                edit_info = Contacts(edit_name, int(input('수정할 전화번호')), input('수정할 이메일'), input('수정할 주소'))

                        ls.append(edit_info)
            else:
                print('잘못된 입력입니다.')
                continue


Contacts.main()
