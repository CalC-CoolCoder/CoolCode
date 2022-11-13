# Algebra and Trigonometry 10-4
def P(x):
    degree = len(coefficients) - 1
    counter = 0
    ans = int(coefficients[0])
    while counter < degree:
        ans *= x
        ans += int(coefficients[counter+1])
        counter += 1
    return ans

print("Find real zeros of P(x) that lie between L and H:")
print("Input the coefficients of P(x) separated by spaces\n\
e.g. Input x^3 - 4x^2 - 5x + 14 as 1 -4 -5 14")
coefficients = input(":: ")
coefficients = coefficients.split()
L = int(input("L = "))
H = int(input("H = "))
x = L
while x <= H:
    if P(x) * P(x+1) <= 0:
        while P(x) * P(x+0.1) > 0:
            x += 0.1
        while P(x) * P(x+0.01) > 0:
            x += 0.01
        while P(x) * P(x+0.001) > 0:
            x += 0.001
        while P(x) * P(x+0.0001) > 0:
            x += 0.0001
        print(round(x, 3))
    x += 1
