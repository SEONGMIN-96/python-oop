class CalculatorConstructor:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        print(c.first)
        print(c.second)
        return c.first + c.second

    def sub(self):
        return c.first - c.second

    def mul(self):
        return c.first * c.second

    def div(self):
        return c.first / c.second

    def avg(self):
        return self.add()/2

if __name__ == '__main__':
    c = CalculatorConstructor(1, 2)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())
    print(c.avg())
