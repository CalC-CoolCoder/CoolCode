# For Algebra and Trigonometry exercise 3-4
print('Find the particular equation of a line from two given points:')
print('(x1, y1) and (x2, y2)')
ans = 'y'
while ans == 'y':
    x1 = int(input('x1 = '))
    y1 = int(input('y1 = '))
    x2 = int(input('x2 = '))
    y2 = int(input('y2 = '))
    if y2 - y1 == 0:
        print('y = ' + str(y1))
    elif x2 - x1 == 0:
        print('x = ' + str(x1))
    else:
        m = (y2 - y1) / (x2 - x1)
        b = -x1 * m + y1
        print('y = ' + str(m) + 'x + ' + str(b))
    ans = input('Find another equation? (y/n) ')
