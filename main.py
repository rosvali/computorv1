import sys
import re

# todo bonus fraction
# - handle decimal periodique

def fraction(dec):
    num = int(str(dec).split(".")[1])
    denom = int("1" + (len(str(num))) * "0")
    rest = int(str(dec).split(".")[0])
    div = num

    if denom > 1000:
        print(dec)
        return()
    while (div > 0):
        if (num % div == 0 and denom % div == 0):
            break
        div -= 1
    print(f"{int((num + rest * denom) / div)}/{int(denom / div)}")

def myabs(nb):
    if nb < 0:
        return(-nb)
    else:
        return(nb)

def mysqrt(nb):
    i = 1
    while i * i < nb:
        i = (i + nb/i) * 0.5 
    return(i)

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
            print("-", end = "") if i == get_degree(equation) else print("-", end = " ")
        if not equation[i] == 0:
            coeff = int(equation[i]) if equation[i].is_integer() else equation[i]
            if i > 1:
                print(f"{myabs(coeff)} * X^{i}", end = " ")
            elif i == 1:
                print(f"{myabs(coeff)} * X", end = " ")
            elif i == 0:
                print(f"{myabs(coeff)}", end = " ")
        if get_degree(equation) == 0 and equation[0] == 0:
            print("0", end = " ")
        i -= 1

def print_solution(solution):
    if solution == 0:
        print(myabs(int(solution)))
    elif solution.is_integer():
        print(int(solution))
    else:
        fraction(solution)

def reduced_form(lequation, requation):
    i = 0
    if len(lequation) < len(requation):
        lequation, requation = swap_equation(lequation, requation)
    print("<=>", end = " ")
    print_equation(lequation)
    print("=", end = " ")
    print_equation(requation)
    for coeff in requation:
        lequation[i] += -coeff
        requation[i] = 0
        if len(requation) > 1:
            print("\n<=>", end = " ")
            print_equation(lequation)
            print("=", end = " ")
            print_equation(requation)
        i += 1
    print("\nReduced form:", end = " ")
    print_equation(lequation)
    print("= 0")
    return(lequation)

def list_equation(side_equation):
    index_coeff = []
    i = 0
    for element in side_equation:
        element = element.replace(" ", "")
        if element == "" and i != 0:
            exit()
        if not element == "+" and not element == "-" and not len(element) == 0:
            element = element.split("*")
            if len(element) > 2:
                exit()
            if len(element) > 1:
                if element[1].lower() == 'x':
                    power = 1
                else:
                    power = element[1].lower().lstrip("x^")
            else:
                power = 0
            if side_equation[i - 1] == "+" or side_equation[i - 1] == "-":
                coeff = side_equation[i - 1] + element[0]
            else:
                coeff = element[0]
            if len(index_coeff) - 1 >= int(power):
                index_coeff[int(power)] += float(coeff)
            else:
                while len(index_coeff) < int(power):
                    index_coeff.insert(len(index_coeff) - 1, 0)
                index_coeff.insert(int(power), float(coeff))
        i += 1
    return(index_coeff)

def parsing_arg(arg):
    parser = r"(([-+=]?)\s*([0-9\.]+)?(\s*\*?\s*[xX](?:\s*\^\s*([0-9]+))?)?\s*)*"
    try:
        res = arg.split("=")
        if len(res) != 2:
            print("Error: need one =")
            exit()
        if re.match(parser, res[0]).group() == res[0] and re.match(parser, res[1]).group() == res[1]:
            lequation = list_equation(re.split("(\+|-)", res[0]))
            requation = list_equation(re.split("(\+|-)", res[1]))
            equation = reduced_form(lequation, requation)
            return (equation)
        else:
            exit()
    except:
        print("Parsing error: please review your equation.")
        exit()

def get_degree(equation):
    i = len(equation) - 1
    while i >= 0:
        if equation[i] == 0:
            i -= 1
        else:
            return(i)
    return(0)

def calc_delta(equation):
    delta = equation[1] * equation[1] - 4 * equation[2] * equation[0]
    print("\n∆ = b^2-4ac")
    print(f"∆ = {equation[1]}^2 - 4 * {equation[2]} * {equation[0]}")
    print(f"∆ = {delta}")
    return(delta)

def second_degree(equation):
    if len(equation) - 1 == 2:
        delta = calc_delta(equation)
        if delta > 0:
            print("\nDiscriminant is strictly positive, the two solutions are:")
            x1 = (-equation[1] - mysqrt(delta)) / (2 * equation[2])
            x2 = (-equation[1] + mysqrt(delta)) / (2 * equation[2])
            print(f"x1 = (-{equation[1]} - √{delta}) / (2 * {equation[2]}) =", end = " ")
            print_solution(x1)
            print(f"x2 = (-{equation[1]} + √{delta}) / (2 * {equation[2]}) =", end = " ")
            print_solution(x2)
        elif delta == 0:
            print("\nDiscriminant is nul, the solution is:")
            x1 = -equation[1]/(2*equation[2])
            print(f"x1 = -({equation[1]}) / (2 * {equation[2]}) =", end = " ")
            print_solution(x1)
        else:
            print("\nDiscriminant is negatif. No solution.")

def solve_equation(equation):
    degree = get_degree(equation)
    if degree >= 1:
        print(f"\nPolynomial degree: {degree}")
    if len(equation) > 3:
        print("\nThe polynomial degree is stricly greater than 2, I can't solve.")
    if degree == 2:
        second_degree(equation)
    if degree == 1:
        x1 = -equation[0] / equation[1]
        print("\nThe solution is:")
        print(f"x1 = -({equation[0]}) / {equation[1]} =", end = " ")
        print_solution(x1)
    if degree == 0:
        print("All numbers are solution.") if equation[0] == 0 else print("It can't solve.")

def main():
    equation = []
    if len(sys.argv) == 2:
        equation = parsing_arg(sys.argv[1])
        solve_equation(equation)
    else:
        print("Error: Need one argument")

main()
fraction(1/3)

# 2 * X^2 + 8 * X^1 + 8 * X^0 = 0 <== delta = 0
# 5 * X^2 - 2 * X^1 + 1 * X^0 = 0 <== delta < 0
# 9 * X^2 - 5 * X^1 + 2 * X^0 = 0 <== delta > 0