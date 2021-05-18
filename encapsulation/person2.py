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
        p = Person(input('회원가입을 위해 성함을 입력해주세요.'), int(input('나이를 적어주세요.')), input('주소를 적어주세요.'))
        print(f'회원님의 성함은:{p.get_name()}')
        print(f'회원님의 나이는:{p.get_age()}')
        print(f'회원님의 주소는:{p.get_address()}')

Person.main()