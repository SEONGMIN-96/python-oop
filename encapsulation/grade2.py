class Grade:
    def set_grade(self, math, eng, kor):
        self.math = math
        self.eng = eng
        self.kor = kor

    def sum(self):
        return g.math + g.eng + g.kor

    def avg(self):
        return (g.sum()/3)

if __name__ == '__main__':
    g = Grade()
    g.set_grade(70, 65, 90)

    print(g.sum())
    print(g.avg())
