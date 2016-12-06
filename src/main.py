#/usr/bin/env python3

import sympy

def parse_expression(latex_string):
    x = sympy.sympify(latex_string)
    return type(x)


def main():
    while True:
        print(parse_expression(input("enter latex string: ")))
    return 0

main()