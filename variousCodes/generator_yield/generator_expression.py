# generator expressions are like list comprehensions but uses () instead of []


gen_expression = (num**2 for num in range(5))
print(next(gen_expression))