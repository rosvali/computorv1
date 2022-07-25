import sys
import equation
import parse
import maths

arg = parse.Parse("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
arg.reduced_form("5 * X^0 + 4 * X^1 - 9.3 * X^2", "1 * X^0")

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