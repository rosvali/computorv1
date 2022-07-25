import sys
import equation
import parse
import maths

def main():
    equation = ""
    print(len(sys.argv))
    if len(sys.argv) == 3:
        equation = parse.Parse(sys.argv[3])
        print(equation.arg)
        print(equation.reduced_form())
    else:
        print("Error: Need an argument")

main()

# arg = parse.Parse("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")

# print(arg.reduced_form("5 * X^0 + 4 * X^1 - 9.3 * X^2", "1 * X^0")) #4.0 * X^0 + 4 * X^1 - 9.3 * X^2

# a, b, c = arg.create_equation("4.0 * X^0 + 4 * X^1 - 9.3 * X^2")
# eq = equation.Equation(a, b, c)

# # eq = equation.Equation("-9.3", "4", "4.0")

# print("a: %s" % (eq.a))
# print("b: %s" % (eq.b))
# print("c: %s" % (eq.c))

# print(f"Delta = {eq.discriminant()}")

# print(f"Racine(s) = {eq.polynome()}")

# print("a is negatif? %s" % (maths.is_negatif(eq.a)))
# print("b is negatif? %s" % (maths.is_negatif(eq.b)))
# print("c is negatif? %s" % (maths.is_negatif(eq.c)))

# print ("Equation:", end = " ")
# eq.display_equation()