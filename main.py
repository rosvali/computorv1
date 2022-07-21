import sys
import equation

eq = equation.Equation("-9.3", "4", "4")

print("a: %s" % (eq.a))
print("b: %s" % (eq.b))
print("c: %s" % (eq.c))

print(f"Delta = {eq.discriminant()}")

print(f"Racine(s) = {eq.polynome()}")

print("a is negatif? %s" % (eq.is_negatif(eq.a)))
print("b is negatif? %s" % (eq.is_negatif(eq.b)))
print("c is negatif? %s" % (eq.is_negatif(eq.c)))

print ("Equation:", end = " ")
eq.display_equation()
