#/usr/bin/env python3

import sympy
from latex2sympy.process_latex import process_sympy

def parse_expression(latex_string):
    return sympy.sympify(process_sympy(latex_string))


def main():
    while True:
        print(sympy.dsolve(parse_expression(input("enter latex string: ")), sympy.abc.x))

main()