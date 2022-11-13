# Algebra and Trigonometry 10-4
print("Solve polynomial P(x) by synthetic substitution:")
print("Input the coefficients of P(x) separated by spaces\n\
e.g. Input x^3 - 4x^2 - 5x + 14 as 1 -4 -5 14")
coefficients = input(":: ")
coefficients = coefficients.split()
degree = len(coefficients) - 1
x = int(input("x = "))
counter = 0
ans = int(coefficients[0])
quotient = []
while counter < degree:
    quotient.append(ans)
    ans *= x
    ans += int(coefficients[counter+1])
    counter += 1
print("P("+str(x)+") =", ans)
print("Coefficients of quotient:", end=" ")
for i in quotient:
    print(i, end=" ")
