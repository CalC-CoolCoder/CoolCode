# For Algebra and Trigonometry exercise 15-6

from math import *

def FND(X):
    return floor(degrees(X))

def FNM(X):
    return (degrees(X) - floor(degrees(X))) * 60

menu = '''ENTER CASE
1 FOR SSS
2 FOR SAS
3 FOR SSA
4 FOR AAS
5 FOR ASA'''
print(menu)
which = input('WHICH? ')

while which in [str(i) for i in range(1,6)]:
    impossible = False
    ambiguous = False
    if which == '1':
        case = 'SSS'
        print('TYPE S1, S2, S3')
        data = input(':: ')
        try:
            data = data.split(', ')
            s1 = float(data[0])
            s2 = float(data[1])
            s3a = float(data[2])
            d1 = FND(acos((s2**2 + s3a**2 - s1**2) / (2*s2*s3a)))
            m1 = FNM(acos((s2**2 + s3a**2 - s1**2) / (2*s2*s3a)))
            d2a = FND(acos((s1**2 + s3a**2 - s2**2) / (2*s1*s3a)))
            m2a = FNM(acos((s1**2 + s3a**2 - s2**2) / (2*s1*s3a)))
            d3a = FND(acos((s2**2 + s1**2 - s3a**2) / (2*s2*s1)))
            m3a = FNM(acos((s2**2 + s1**2 - s3a**2) / (2*s2*s1)))
            area1 = (1/2) * s2 * s3a * sin(radians(d1 + (m1/60)))
        except:
            impossible = True
    elif which == '2':
        case = 'SAS'
        print('TYPE S1, D3 M3, S2')
        data = input(':: ')
        try:
            data = data.split(', ')
            s1 = float(data[0])
            d3a = int(data[1].split()[0])
            m3a = float(data[1].split()[1])
            s2 = float(data[2])
            s3a = sqrt(s1**2 + s2**2 - 2*s1*s2*cos(radians(d3a + (m3a/60))))
            d1 = FND(acos((s2**2 + s3a**2 - s1**2) / (2*s2*s3a)))
            m1 = FNM(acos((s2**2 + s3a**2 - s1**2) / (2*s2*s3a)))
            d2a = FND(acos((s1**2 + s3a**2 - s2**2) / (2*s1*s3a)))
            m2a = FNM(acos((s1**2 + s3a**2 - s2**2) / (2*s1*s3a)))
            area1 = (1/2) * s2 * s3a * sin(radians(d1 + (m1/60)))
        except:
            impossible = True
    elif which == '3':
        case = 'SSA'
        print('TYPE S1, S2, D1 M1')
        data = input(':: ')
        try:
            data = data.split(', ')
            s1 = float(data[0])
            s2 = float(data[1])
            d1 = int(data[2].split()[0])
            m1 = float(data[2].split()[1])
            s3a = (2*s2*cos(radians(d1+(m1/60))) + sqrt((2*s2*cos(radians(d1+(m1/60))))**2 - 4 * (s2**2 - s1**2))) / 2
            s3b = (2*s2*cos(radians(d1+(m1/60))) - sqrt((2*s2*cos(radians(d1+(m1/60))))**2 - 4 * (s2**2 - s1**2))) / 2
            d2a = FND(acos((s1**2 + s3a**2 - s2**2) / (2*s1*s3a)))
            m2a = FNM(acos((s1**2 + s3a**2 - s2**2) / (2*s1*s3a)))
            d3a = FND(acos((s2**2 + s1**2 - s3a**2) / (2*s2*s1)))
            m3a = FNM(acos((s2**2 + s1**2 - s3a**2) / (2*s2*s1)))
            area1 = (1/2) * s2 * s3a * sin(radians(d1 + (m1/60)))
            if s3b > 0:
                ambiguous = True
                d2b = FND(acos((s1**2 + s3b**2 - s2**2) / (2*s1*s3b)))
                m2b = FNM(acos((s1**2 + s3b**2 - s2**2) / (2*s1*s3b)))
                d3b = FND(acos((s2**2 + s1**2 - s3b**2) / (2*s2*s1)))
                m3b = FNM(acos((s2**2 + s1**2 - s3b**2) / (2*s2*s1)))
                area2 = (1/2) * s2 * s3b * sin(radians(d1 + (m1/60)))
        except:
            impossible = True
    elif which == '4':
        case = 'AAS'
        print('TYPE D1 M1, D2 M2, S1')
        data = input(':: ')
        try:
            data = data.split(', ')
            d1 = int(data[0].split()[0])
            m1 = float(data[0].split()[1])
            d2a = int(data[1].split()[0])
            m2a = float(data[1].split()[1])
            s1 = float(data[2])
            d3a = floor(180 - (d1 + (m1/60)) - (d2a + (m2a/60)))
            m3a = ((180 - (d1 + (m1/60)) - (d2a + (m2a/60))) - floor(180 - (d1 + (m1/60)) - (d2a + (m2a/60)))) * 60
            s2 = (s1 * sin(radians(d2a + (m2a/60)))) / sin(radians(d1 + (m1/60)))
            s3a = (s1 * sin(radians(d3a + (m3a/60)))) / sin(radians(d1 + (m1/60)))
            area1 = (1/2) * s2 * s3a * sin(radians(d1 + (m1/60)))
        except:
            impossible = True
    elif which == '5':
        case = 'ASA'
        print('TYPE D1 M1, S3, D2 M2')
        data = input(':: ')
        try:
            data = data.split(', ')
            d1 = int(data[0].split()[0])
            m1 = float(data[0].split()[1])
            s3a = float(data[1])
            d2a = int(data[2].split()[0])
            m2a = float(data[2].split()[1])
            d3a = floor(180 - (d1 + (m1/60)) - (d2a + (m2a/60)))
            m3a = ((180 - (d1 + (m1/60)) - (d2a + (m2a/60))) - floor(180 - (d1 + (m1/60)) - (d2a + (m2a/60)))) * 60
            s1 = (s3a * sin(radians(d1 + (m1/60)))) / sin(radians(d3a + (m3a/60)))
            s2 = (s3a * sin(radians(d2a + (m2a/60)))) / sin(radians(d3a + (m3a/60)))
            area1 = (1/2) * s2 * s3a * sin(radians(d1 + (m1/60)))
        except:
            impossible = True
    print('CASE:', case)
    if impossible:
        print('No such triangle')
    else:
        print('S1 =', round(s1, 3))
        print('S2 =', round(s2, 3))
        print('S3 =', round(s3a, 3))
        print('A1 =', str(d1) + 'D,', '%02d' % round(m1) + 'M')
        print('A2 =', str(d2a) + 'D,', '%02d' % round(m2a) + 'M')
        print('A3 =', str(d3a) + 'D,', '%02d' % round(m3a) + 'M')
        print('AREA =', round(area1, 3))
        if ambiguous:
            print('or:')
            print('S1 =', round(s1, 3))
            print('S2 =', round(s2, 3))
            print('S3 =', round(s3b, 3))
            print('A1 =', str(d1) + 'D,', '%02d' % round(m1) + 'M')
            print('A2 =', str(d2b) + 'D,', '%02d' % round(m2b) + 'M')
            print('A3 =', str(d3b) + 'D,', '%02d' % round(m3b) + 'M')
            print('AREA =', round(area2, 3))
    print('\n' + menu)
    which = input('WHICH? ')
