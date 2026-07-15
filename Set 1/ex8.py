# 8. Given a string that represents a polynomial (Ex: "3x^3 + 5x^2 - 2x - 5")
# and a number (int or float), evaluate the polynomial for the given value.

import re


def evaluate_polynomial(poly_str: str, x_value):
    """Evaluate a polynomial given as a string (e.g. '3x^3 + 5x^2 - 2x - 5') at x_value."""
    poly_str = poly_str.replace(' ', '')
    # Turn "a - b" into "a + -b" so we can split cleanly on "+"
    poly_str = poly_str.replace('-', '+-')
    if poly_str.startswith('+'):
        poly_str = poly_str[1:]

    terms = [term for term in poly_str.split('+') if term]

    # Matches either "<coeff>x^<power>" / "<coeff>x" or a plain constant "<coeff>"
    term_pattern = re.compile(r'^(-?\d*)x(?:\^(-?\d+))?$|^(-?\d+)$')

    total = 0
    for term in terms:
        match = term_pattern.match(term)
        if not match:
            raise ValueError(f"Invalid term in polynomial: {term}")

        if match.group(3) is not None:
            total += int(match.group(3))
        else:
            coeff_str = match.group(1)
            if coeff_str in ('', '+'):
                coeff = 1
            elif coeff_str == '-':
                coeff = -1
            else:
                coeff = int(coeff_str)
            power = int(match.group(2)) if match.group(2) else 1
            total += coeff * (x_value ** power)

    return total


polynomial = "3x^3 + 5x^2 - 2x - 5"
value = 2
print('\n Exercise 8')
print(f' The polynomial "{polynomial}" evaluated at x={value} is: {evaluate_polynomial(polynomial, value)}')