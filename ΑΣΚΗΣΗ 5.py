import random
print('Δώσε τις πλευρές του ορθωγωνίου:')
platos = int(input('πλάτος: '))
while platos < 0:
    platos = int(input('Δώσε θετικό αριθμό για πλάτος: '))
mikos = int(input('Μήκος: '))
while mikos < 0:
  mikos = int(input('Δώσε θετικό αριθμό για μήκος: '))
synolo100 = 0
epanal=100
for k in range(epanal):
  panel = []
  for i in range(platos):
      panel.append(['O'] * mikos)
  y = 0
  misa = int((platos*mikos)/2)+((platos*mikos) % 2 > 0)
  while y < misa:
      r1 = random.randrange(0, platos)
      r2 = random.randrange(0, mikos)
      if panel[r1][r2] != 'S':
          panel[r1][r2] = 'S'
          y = y + 1
  print('__________________________________')
  for i in range(platos):
      print(panel[i])
  print('__________________________________')
  orizontia = 0
  katheta = 0
  diagwnia = 0
  for i in range(platos):
    for j in range(mikos-2):
      if panel[i][j]=='S':
        if panel[i][j+1]=='O':
          if panel[i][j+2]=='S':
            orizontia +=1
  print('Οριζόντια SOS:', orizontia)
  for i in range(mikos):
      c = 0
      for j in range(platos):
          if panel[j][i] == 'S':
              if c == 2:
                  katheta += 1
              c=1
          else:
              if c == 1:
                  c = 2
              else:
                  c = 0
  print('Κάθετα SOS:', katheta)
  for i in range(platos - 2):
      for j in range(mikos - 2):
          if panel[i][j] == 'S':
              if panel[i + 1][j + 1] == 'O':
                  if panel[i + 2][j + 2] == 'S':
                      diagwnia += 1
  for i in reversed(range(platos - 2)):
      for j in reversed(range(2, mikos)):
          if panel[i][j] == 'S':
              if panel[i + 1][j - 1] == 'O':
                  if panel[i + 2][j - 2] == 'S':
                      diagwnia += 1
  print('Διαγώνια SOS:', diagwnia)
  sos = orizontia + katheta + diagwnia
  synolo100 += sos
print('____________________________________________________')
print('Συνολικές τριάδες SOS απο όλες τις επαναλήψεις:', synolo100)
print('Μέσος όρος:', synolo100/epanal)