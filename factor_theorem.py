# For Algebra and Trigonometry exercise 7-6

def P(x):
    return A*x**3 + B*x**2 + C*x + D

print("Search for linear factors of the form (x - n) for \
cubic polynomials of the form")
print("P(x) = Ax^3 + Bx^2 + Cx + D")
print("using the Factor Theorem:")

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
D = int(input("D = "))
K = 0
X = 1

while X <= abs(D):
    if D % X == 0:
        Y = P(X)
        if Y == 0:
            print("X -", X)
            K += 1
        Y = P(-X)
        if Y == 0:
            print("X +", X)
            K += 1
    X += 1

if not K > 0:
    print("NO FACTORS (X - N)")
