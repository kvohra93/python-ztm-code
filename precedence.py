# understanding operator precedence
# prints 45.0
print((5 + 4) * 10 / 2)
# prints 45.0
print(((5 + 4) * 10) / 2)
# prints 45.0
print((5 + 4) * (10 / 2))
# prints 25.0
print(5 + (4 * 10) / 2)
# prints 25 
print(5 + 4 * 10 // 2)
