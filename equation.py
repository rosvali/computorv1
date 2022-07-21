from math import sqrt

class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return float(self.b) ** 2 - 4 * float(self.a) * float(self.c)

    def polynome(self):
        delta = self.discriminant()

        if delta < 0:
            return None, None

        elif delta == 0:
            return -(float(self.b))/(2*a), None

        else:
            x1 = (-int(self.b) - sqrt(delta)) / (2 * float(self.a))
            x2 = (-int(self.b) + sqrt(delta)) / (2 * float(self.a))
            return x1, x2

    def is_negatif(self, nb):
        return True if nb[0] == '-' else False

    def display_equation(self):
        print(f"{self.a}X^2", end = " ")
        print(f"- {self.b[1:]}X", end = " ") if self.is_negatif(self.b) else print(f"+ {self.b}X", end = " ")
        print(f"- {self.c[1:]}") if self.is_negatif(self.c) else print(f"+ {self.c}")