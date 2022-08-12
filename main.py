import sys
import re
from math import sqrt

# todo handle X^-1 / X^1.2
# todo sqrt function

def swap_equation(lequation, requation):
    tmp = lequation
    lequation = requation
    requation = tmp
    return(lequation, requation)

def print_equation(equation):
    i = len(equation) - 1
    while(i >= 0):
        if i < len(equation) - 1 and equation[i] > 0:
            print("+", end = " ")
        elif equation[i] < 0:
            print("-", end = " ")
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

def print_degree(equation):
    print(f"Polynomial degree: {len(equation) - 1}")
    if len(equation) > 3:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
    return(len(equation) - 1)

def calc_delta(equation):
    return(equation[1] ** 2 - 4 * equation[2] * equation[0])

def second_degree(equation):
    if len(equation) - 1 == 2:
        delta = calc_delta(equation)
        if delta > 0:
            print("Discriminant is strictly positive, the two solutions are:")
            x1 = (-equation[1] - sqrt(delta)) / (2 * equation[2])
            x2 = (-equation[1] + sqrt(delta)) / (2 * equation[2])
            print(x1)
            print(x2)
        elif delta == 0:
            print("Discriminant is nul, the solution is:")
            x1 = -equation[1]/(2*equation[2])
            print(x1)
        else:
            print("Discriminant is negatif. No solution.")

def solve_equation(equation):
    degree = len(equation) - 1
    if degree == 2:
        second_degree(equation)

def main():
    equation = []
    if len(sys.argv) == 2:
        equation = parsing_arg(sys.argv[1])
        if print_degree(equation) <= 2:
            solve_equation(equation)
    else:
        print("Error: Need one argument")

main()

# 2 * X^2 + 8 * X^1 + 8 * X^0 = 0 <== delta = 0
# 5 * X^2 - 2 * X^1 + 1 * X^0 = 0 <== delta < 0
# 9 * X^2 - 5 * X^1 + 2 * X^0 = 0 <== delta > 0