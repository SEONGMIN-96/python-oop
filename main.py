class Stock(object):

    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def get_per(self):
        return self.per

    def get_pbr(self):
        return self.pbr

    def get_배당수익률(self):
        return self.배당수익률

    @staticmethod
    def main():
        s = Stock(input('종목명을 적어주십시오'), int(input('종목코드를 적어주십시오.')), int(input('per을 적어주십시오')), int(input('pbr을 적어주십시오')), int(input('배당수익률을 적어주십시오')))
        print(f'종목명은 {s.get_name()}')
        print(f'종목코드는 {s.get_code()}')
        print(f'per는 {s.get_per()}')
        print(f'pbr는 {s.get_pbr()}')
        print(f'배당수익률 {s.get_배당수익률()}')


Stock.main()