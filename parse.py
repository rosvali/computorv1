import re
import equation

class Parse:
    def __init__(self, arg):
        self.arg = arg

    def get_degree(self, str):
        i = 0
        degree = -1
        while (i != len(str)):
            if(str[i] == '^'):
                degree = int(str[i + 1])
            i += 1
        print(f"Polynomial degree: {degree}")
        return (degree)

    def reduced_form(self):
        res = self.arg.split(" = ")
        requation = res[0].split(" ")
        lequation = res[1].split(" ")
        i = 0
        for element in lequation:
            if (i < len(lequation) and re.match(r"[X]\^[0-9]", element)):
                if element in requation:
                    if re.match("-|\+", lequation[i - 3]):
                        temp = float(lequation[i - 3] + lequation[i - 2]) * -1
                        requation[requation.index(element) - 2] = str(float(requation[requation.index(element) - 2]) + temp)
                    else:
                        temp = float(lequation[i - 2]) * -1
                        requation[requation.index(element) - 2] = str(float(requation[requation.index(element) - 2]) + temp)
                else:
                    requation.append(lequation[i - 3])
                    requation.append(lequation[i - 2])
                    requation.append(lequation[i - 1])
                    requation.append(lequation[i])
            i += 1
        reduced = " ".join(requation)
        print(f"Reduced form: {reduced} = 0")
        return(reduced)

    def create_equation(self, equation):
        a = 0
        b = 0
        c = 0
        i = 0
        equ_list = equation.split(" ")
        for element in equ_list:
            if element == "X^2":
                a = equ_list[i - 2]
                a = "-" + a if equ_list[i - 3] == '-' else a
            if element == "X^1":
                b = equ_list[i - 2]
                b = "-" + b if equ_list[i - 3] == '-' else b
            if element == "X^0":
                c = equ_list[i - 2]
                c = "-" + c if equ_list[i - 3] == '-' else c
            i += 1
        return a, b, c

    def parsing_equation(self):
        reduced_form = self.reduced_form()
        if self.get_degree(reduced_form) < 3:
            create_equation(reduced_form)
        else:
            print("The polynomial degree is stricly greater than 2, I can't solve.")