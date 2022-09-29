# Computorv1 testing

## Input list

- Argument error

```
python3 computor.py
Error: Need one argument

python3 computor.py "X = 0" "4 * 5 = 0"
Error: Need one argument
```

- Bad syntax

```
python3 computor.py "1 * r 5 + 4 d = p 0"
python3 computor.py "4 **** X + 1 = X + 1"
python3 computor.py "4 = -4 + -5"
python3 computor.py "2 * X^^^1 = 1"
python3 computor.py "2X = 65"
python3 computor.py "543"
python3 computor.py " X = 1 = 1"
python3 computor.py "xx = 0"
python3 computor.py "x == 0"
python3 computor.py "1/2 * X = 1"
python3 computor.py "4 * 5 = x"
python3 computor.py "43,3 = x"
```

- Good syntax

```
python3 computor.py "1 * X^0 + 3 * X^1 - 2 * X^2 = 0"
python3 computor.py "X + 3 = X^2 - 5"
python3 computor.py "   2 * X   ^  2   =  -  6  -  5 * X"
python3 computor.py "3 * x = 34 + x - 1 + X^2"
python3 computor.py "4 * x1 + x2 = 9"
python3 computor.py "3*x-5+4=45*x"
python3 computor.py "54.5 - 3 = 4 * X^1"
```

- first degree equation

```
python3 computor.py "X = 3 + 5 + 2 * X"
python3 computor.py "3 + 5 * x - 3 * x = 12 + 4 * x"
python3 computor.py "4 + 5 = x"
```

- second degree equation

delta < 0
```
python3 computor.py "X^2 + 5 = X^1 -6 + 4 * X"
delta = -19
```

delta = 0
```
python3 computor.py "2 * X^2 + 8 * X^1 + 8 * X^0 = 0"
delta = 0
```

delta > 0
```
python3 computor.py "5 * X^2 + 3 * X + 0 = 9"
delta = 189
```

- others

```
python3 computor.py "42 = 42"
python3 computor.py "42 * X^0 = 42 * X^0"
All numbers are solution
python3 computor.py "1 = 0"
No solution
```

- Bonus
    - Gerer les erreurs d'entrees
    - Gerer les entrees et sorties sous forme naturelle
    - Fraction
    - Etapes intermediaires