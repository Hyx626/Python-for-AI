# List conprehension = A concise way to create list in Python
#                     compact and easier to read than tranditional loops
#                     [exprssion for value in interable if condition]

# [exprssion for value in interable if condition]
# doubles = [x * 2 for x in range(1, 11)]
# triples = [e * 3 for e in range(1, 11)]
# squares = [y ** y for y in range(1, 11)]


fruits = ["apple", "banana", "orange", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)