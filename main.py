import sys
import equation
import parse
import maths
import re

# todo handle X^-1 / X^1.2

def swap_equation(lequation, requation):
    tmp = lequation
    lequation = requation
    requation = tmp
    return(lequation, requation)

def print_equation(equation):
    i = len(equation) - 1
    while(i >= 0):
        print("+", end = " ") if i != len(equation) - 1 and equation[i] > 0 else print("-", end = " ")
        print(f"{abs(equation[i])} * X^{i}", end = " ")
        i -= 1

def reduced_form(lequation, requation):
    i = 0
    if len(lequation) < len(requation):
        lequation, requation = swap_equation(lequation, requation)
    for coeff in requation:
        lequation[i] += coeff
        requation[i] = 0
        i += 1
    print("Reduced form:", end = " ")
    print_equation(lequation)
    print("= 0")
    return(lequation)

def table_arg(side_equation):
    index_tokens = []
    i = 0
    for element in side_equation:
        if element.find("X^") != -1:
            if re.match("\+|-", side_equation[i - 3]):
                side_equation[i - 2] = side_equation[i - 3] + side_equation[i - 2]
            if len(index_tokens) > int(element[-1]):
                index_tokens[int(element[-1])] += float(side_equation[i - 2])
            else:
                while len(index_tokens) < float(element[-1]):
                    index_tokens.insert(len(index_tokens) - 1, 0)
                index_tokens.insert(int(element[-1]), float(side_equation[i - 2]))
        i += 1
    return(index_tokens)

def parsing_arg(arg):
    res = arg.split(" = ")
    lequation = table_arg(re.split(" ", res[0]))
    requation = table_arg(re.split(" ", res[1]))
    equation = reduced_form(lequation, requation)
    return (equation)

def main():
    equation = []
    if len(sys.argv) == 2:
        equation = parsing_arg(sys.argv[1])
    else:
        print("Error: Need one argument")

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