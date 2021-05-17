class Grade:
    def set_grade(self, math, eng, kor):
        self.math = math
        self.eng = eng
        self.kor = kor

    def sum(self):
        return self.math + self.eng + self.kor

    def avg(self):
        return (self.sum()/3)

if __name__ == '__main__':
    g = Grade()
    g.set_grade(70, 60, 50)

    print(g.sum())
    print(g.avg())