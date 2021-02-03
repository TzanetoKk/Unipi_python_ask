import random
print('Δώσε την πλευρά του τετραγώνου:')
pleyra = int(input('> '))
while pleyra < 0:
    print('Δώσε θετικό αριθμό')
    pleyra = int(input('> '))
synolo100 = 0
epanal = 100
for k in range(epanal):
    numbers = []
    for i in range(pleyra):
        numbers.append([0] * pleyra)
    misa = int((pleyra**2)/2)+((pleyra**2) % 2 > 0)
    y = 0
    while y < misa:
        r1 = random.randrange(0, pleyra)
        r2 = random.randrange(0, pleyra)
        if numbers[r1][r2] != 1:
            numbers[r1][r2] = 1
            y += 1
    print('__________________________________')
    for i in range(pleyra):
        print(numbers[i])
    print('__________________________________')
    katheta = 0
    orizontia = 0
    diagwnia = 0

    for i in range(pleyra):
        c = 0
        for j in range(pleyra):
            if numbers[i][j] == 1:
                c = c + 1
                if c == 4:
                    orizontia += 1
                    c = 0
            else:
                c = 0
    print('Οριζόντιες τετράδες:', orizontia)
    for i in range(pleyra):
        c = 0
        for j in range(pleyra):
            if numbers[j][i] == 1:
                c = c + 1
                if c == 4:
                    katheta += 1
                    c = 0
            else:
                c = 0
    print('Κάθετες τετράδες:', katheta)
    for i in range(pleyra - 3):
        for j in range(pleyra - 3):
            if i == 0 or j == 0:
                if numbers[i][j] == numbers[i + 1][j + 1]:
                    if numbers[i][j] == numbers[i + 2][j + 2]:
                        if numbers[i][j] == numbers[i + 3][j + 3]:
                            if numbers[i][j] == 1:
                                diagwnia += 1
            else:
                if numbers[i][j] == 1:
                    if numbers[i - 1][j - 1] != 1:
                        if numbers[i][j] == numbers[i + 1][j + 1]:
                            if numbers[i][j] == numbers[i + 2][j + 2]:
                                if numbers[i][j] == numbers[i + 3][j + 3]:
                                    diagwnia += 1
    for i in reversed(range(pleyra - 3)):
        for j in reversed(range(3, pleyra)):
            if i == 0 or j == pleyra-1:
                if numbers[i][j] == 1:
                    if numbers[i][j] == numbers[i + 1][j - 1]:
                        if numbers[i][j] == numbers[i + 2][j - 2]:
                            if numbers[i][j] == numbers[i + 3][j - 3]:
                                diagwnia += 1
            else:
                if numbers[i][j] == 1:
                    if numbers[i - 1][j + 1] != 1:
                        if numbers[i][j] == numbers[i + 1][j - 1]:
                            if numbers[i][j] == numbers[i + 2][j - 2]:
                                if numbers[i][j] == numbers[i + 3][j - 3]:
                                    diagwnia += 1
    print('Διαγώνιες τετράδες:', diagwnia)
    synolo = katheta + orizontia + diagwnia
    synolo100 += synolo
print('_________________________________________________')
print('Συνολικές τετράδες απο όλες τις επαναλήψεις:', synolo100)
print('Μέσος όρος:', synolo100/epanal)