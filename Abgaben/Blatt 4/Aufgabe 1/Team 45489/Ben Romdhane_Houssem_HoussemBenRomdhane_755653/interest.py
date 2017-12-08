import math


def current_value(a_0, p, n):
    "The function current_value calculates the real value from the initial value a_0, the interest rate p and the number of years n"
    return a_0 * ((1 + (p/(360 * 100))) ** n)


def initial_value(a, p, n):
    "The function initial_value calculates the initial value from the real value, the interest rate p and the number of years n"
    return a * (1 + (p/(360 * 100))) ** (-n)


def number_of_years(a, a_0, p):
    "The function number_of_years calculates the number of years needed to reach a real value a from an initial value a_0 and an interest rate p"
    return math.log(a/a_0)/math.log(1+(p/(360*100)))


def interest_rate(a, a_0, n):
    "The function interest_rate calculates the interest rate corresponding to an increase of an initial value a_0 to a real value a in a number n of years"
    return 360 * 100 * (((a/a_0) ** (1.0/n)) - 1)

