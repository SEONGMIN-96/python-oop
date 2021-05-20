class Grade(object):

    def __init__(self, math, eng, kor):
        self.math = math
        self.eng = eng
        self.kor = kor

    def sum(self):
        return self.math + self.eng + self.kor

    def avg(self):
        return self.sum()/3

    def get_grade(self):
        score = int(self.avg())
        if score > 95:
            grade = 'A학점'
        elif score >= 85:
            grade = 'B학점'
        elif score >= 75:
            grade = 'C학점'
        elif score >= 65:
            grade = 'D학점'
        else:
            grade = 'F학점'

        return grade

    @staticmethod
    def main():
        g = Grade(int(input('수학점수:')), int(input('영어점수:')), int(input('국어점수:')))
        print(f'총점:{g.sum()}')
        print(f'평균:{g.avg()}')
        print(f'학점:{g.get_grade()}')

Grade.main()



