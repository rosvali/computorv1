import sys
import equation
import maths

class Parse:
    def __init__(self, arg):
        self.arg = arg

    def list_to_string(self, list):
        str = ""
        for i in list:
            str += i
        return str

    def split_block(self, res):
        res = res.split('+')
        res = self.list_to_string(res)
        res = res.split('-')
        print(res)
        return res

    def reduced_form(self):
        res = self.arg.split('=')
        # print(res) # ['5 * X^0 + 4 * X^1 - 9.3 * X^2 ', ' 1 * X^0']
        res2 = self.split_block(res[1])
        # print(res2)

# arg = Parse("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
arg = Parse("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 + 1 + 2 - 4 + 6")
arg.reduced_form()

eq = equation.Equation("-9.3", "4", "4")

print("a: %s" % (eq.a))
print("b: %s" % (eq.b))
print("c: %s" % (eq.c))

print(f"Delta = {eq.discriminant()}")

print(f"Racine(s) = {eq.polynome()}")

print("a is negatif? %s" % (maths.is_negatif(eq.a)))
print("b is negatif? %s" % (maths.is_negatif(eq.b)))
print("c is negatif? %s" % (maths.is_negatif(eq.c)))

print ("Equation:", end = " ")
eq.display_equation()
 