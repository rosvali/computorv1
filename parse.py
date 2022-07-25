import equation

class Parse:
    def __init__(self, arg):
        self.arg = arg
        self.reduced_form()

    def get_degree(self, str):
        i = 0
        degree = -1
        while (i != len(str)):
            if(str[i] == '^'):
                degree = int(str[i + 1])
            i += 1
        return (degree)

    def reduced_form(self):
        res = self.arg.split(" = ")
        requation = res[0].split(" ")
        lequation = res[1].split(" ")
        i = 2
        for element in requation and lequation:
            if ((i - 2) < len(requation) and (i - 2) < len(lequation)):
                if (element == "X^0" or element == "X^1" or element == "X^2"):
                    temp = float(lequation[i - 4]) * -1
                    requation[i - 4] = str(float(requation[i - 4]) + temp)
            i += 1
        reduced = " ".join(requation)
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
