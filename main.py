import sys
import equation
import parse
import maths
import re

# todo handle power negatif and float

def table_arg(side_equation):
    index_tokens = []
    i = 0
    for element in side_equation:
        if element.find("X^") != -1:
            if re.match("\+|-", side_equation[i - 3]):
                side_equation[i - 2] = side_equation[i - 3] + side_equation[i - 2]
            if len(index_tokens) > int(element[-1]):
                index_tokens[float(element[-1])] += float(side_equation[i - 2])
            else:
                while len(index_tokens) < float(element[-1]):
                    index_tokens.insert(len(index_tokens) - 1, 0)
                index_tokens.insert(float(element[-1]), float(side_equation[i - 2]))
        i += 1
    print(index_tokens)

def parsing_argv(arg):
    res = arg.split(" = ")
    lequation = re.split(" ", res[0])
    requation = re.split(" ", res[1])
    print(lequation, requation)
    lequation = table_arg(lequation)
    requation = table_arg(requation)
    
def main():
    parsing = ""
    equat = ""
    if len(sys.argv) == 2:
        print(sys.argv[1])
        parsing_argv(sys.argv[1])
        # parsing = parse.Parse(sys.argv[1]).parsing_equation()
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