'''
이름, 출생년도, 주소를 입력받아서
회원가입한 사람의 이름, 나이(만), 주소를 출력하시오.
'''

class Person(object):

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_name(self):
        return self.name

    def get_age(self):
        return 2021 - self.age

    def get_address(self):
        return self.address

    @staticmethod
    def main():
        p = Person(input('회원가입을위해 성함을입력하세요.'), int(input('나이를입력하세요.')), input('주소를입력하세요.'))
        print(f'고객님의 성함은:{p.get_name()}')
        print(f'고객님의 나이는:{p.get_age()}')
        print(f'고객님의 주소는:{p.get_address()}')

Person.main()



