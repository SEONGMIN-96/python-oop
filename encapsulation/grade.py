class Grade:

    def __init__(self, math, eng, kor):
        self.math = math
        self.eng = eng
        self.kor = kor

    def sum(self):
        return self.math + self.eng + self.kor

    def avg(self):
        return self.sum() / 3

    def get_grade(self):
        score = int(self.avg())
        grade = ''
        if score > 98:
           grade = 'A학점'

        return grade

    @staticmethod
    def main():
        g = Grade(int(input()), int(input()), int(input()))
        print('총점수:', g.sum())
        print('평균:', g.avg())
        print(f'학점: {g.get_grade()}')

Grade.main()
