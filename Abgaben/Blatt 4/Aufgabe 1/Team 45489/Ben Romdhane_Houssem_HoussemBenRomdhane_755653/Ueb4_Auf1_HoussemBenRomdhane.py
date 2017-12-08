import interest

p = 0.1
a_0 = 1000
n = 10.0


help(interest.current_value)
help(interest.initial_value)
help(interest.number_of_years)
help(interest.interest_rate)

print("Value after 10 years: {}".format(interest.current_value(a_0, p, n)))
print("Number of years necessary for the initial value to double: {} years".format(interest.number_of_years(2 * a_0, a_0, p)))

