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
        return (degree)

    def reduced_form(self, requation, lequation):
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