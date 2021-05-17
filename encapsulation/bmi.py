class Bmi:
    def set_figure(self, weight, tall):
        self.weight = weight
        self.tall = tall

    def val_tall(self):
        return self.tall/100

    def mul_tall(self):
        return self.val_tall() * self.val_tall()

    def avg(self):
        return self.weight / self.mul_tall()

if __name__ == '__main__':
    b = Bmi()
    b.set_figure(62, 168)
    print(b.avg())