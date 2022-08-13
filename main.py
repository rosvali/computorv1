from math import sqrt
import sys
import re

# todo handle X^-1 / X^1.2
# todo sqrt function
# todo handle a = 0

def swap_equation(lequation, requation):
    tmp = lequation
    lequation = requation
    requation = tmp
    return(lequation, requation)

def print_equation(equation):
    i = get_degree(equation)
    while(i >= 0):
        if i < get_degree(equation) and equation[i] > 0:
            print("+", end = " ")
        elif equation[i] < 0:
            print("-", end = " ")
        if not equation[i] == 0:
            coeff = int(equation[i]) if equation[i].is_integer() else equation[i]
            print(f"{abs(coeff)} * X^{i}", end = " ")
        if get_degree(equation) == 0 and equation[0] == 0:
            print("0", end = " ")
        i -= 1

def print_solution(solution):
    if solution == 0:
        print(abs(int(solution)))
    elif solution.is_integer():
        print(int(solution))
    else:
        print(solution)

def reduced_form(lequation, requation):
    i = 0
    if len(lequation) < len(requation):
        lequation, requation = swap_equation(lequation, requation)
    for coeff in requation:
        lequation[i] += -coeff
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

def get_degree(equation):
    i = len(equation) - 1
    while i >= 0:
        if equation[i] == 0:
            i -= 1
        else:
            return(i)
    return(0)

def calc_delta(equation):
    return(equation[1] ** 2 - 4 * equation[2] * equation[0])

def second_degree(equation):
    if len(equation) - 1 == 2:
        delta = calc_delta(equation)
        if delta > 0:
            print("Discriminant is strictly positive, the two solutions are:")
            x1 = (-equation[1] - sqrt(delta)) / (2 * equation[2])
            x2 = (-equation[1] + sqrt(delta)) / (2 * equation[2])
            print_solution(x1)
            print_solution(x2)
        elif delta == 0:
            print("Discriminant is nul, the solution is:")
            x1 = -equation[1]/(2*equation[2])
            print_solution(x1)
        else:
            print("Discriminant is negatif. No solution.")

def solve_equation(equation):
    degree = get_degree(equation)
    print(f"Polynomial degree: {degree}")
    if len(equation) > 3:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
    if degree == 2:
        second_degree(equation)
    if degree == 1:
        x1 = -equation[0] / equation[1]
        print("The solution is:")
        print_solution(x1)
    if degree == 0:
        print("All numbers are solution.")

def main():
    equation = []
    if len(sys.argv) == 2:
        equation = parsing_arg(sys.argv[1])
        if get_degree(equation) <= 2:
            solve_equation(equation)
    else:
        print("Error: Need one argument")

main()

# 2 * X^2 + 8 * X^1 + 8 * X^0 = 0 <== delta = 0
# 5 * X^2 - 2 * X^1 + 1 * X^0 = 0 <== delta < 0
# 9 * X^2 - 5 * X^1 + 2 * X^0 = 0 <== delta > 0