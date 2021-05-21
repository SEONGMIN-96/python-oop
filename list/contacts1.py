"""
이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제, 수정하는 프로그램을 완성하시오.
"""


class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def string_contacts(self):
        return f'name: {self.name}, phone: {self.phone}, email: {self.email}, address: {self.address}'

    @staticmethod
    def del_element(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.exit 1.create 2.read 3.update 4.delete')
            if menu == '0':
                print('종료합니다.')
                break
            elif menu == '1':
                ls.append(Contacts(input('name'), int(input('phone')), input('email'), input('address')))
            elif menu == '2':
                for i in ls:
                    print(i.string_contacts())
            elif menu == '3':
                name = input('수정할 이름')
                edit_info = Contacts(name, int(input('수정할 전화번호')), input('수정할 이메일'), input('수정할 주소'))
                Contacts.del_element(ls, name)
                ls.append(edit_info)
            elif menu == '4':
                name = input('수정할 이름')
                Contacts.del_element(ls, name)


Contacts.main()