# For Algebra and Trigonometry exercise 4-3
print('Solve a system of two linear equations with two variables:')
print('ax + by = c\ndx + ey = f')
ans = 'y'
while ans == 'y':
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    d = int(input('d = '))
    e = int(input('e = '))
    f = int(input('f = '))
    D = a * e - b * d
    Nx = c * e - b * f
    Ny = a * f - c * d
    print('D = ' + str(D))
    print('Nx = ' + str(Nx))
    print('Ny = ' + str(Ny))
    if D == 0:
        if Nx == 0:
            print('DEPENDENT')
        else:
            print('INCONSISTENT')
    else:
        print('S = {(' + str(Nx / D) + ', ' + str(Ny / D) + ')}')
    ans = input('Solve another system? (y/n) ')
