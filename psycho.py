import pandas as pd

x = pd.read_csv('psycho.csv', sep = ';', header = None).values.tolist()

count_psychotism = 0
count_extraverse = 0
count_neyrotism = 0
count_sincerity = 0
for i in x:
    if x.index(i) in [2, 6, 9,11, 19, 39, 43, 59,63,67,78,100] and i[1] == ' -':
        count_psychotism += 1
    if x.index(i) in [14, 23,27, 31, 35, 47, 51, 53] and i[1] == ' +':
        count_psychotism += 1
    if x.index(i) in [22, 30, 46, 84] and i[1] == ' -':
        count_extraverse += 1
    if x.index(i) in [1,3,10, 15,18, 26, 34, 38, 42, 50] and i[1] == ' +':
        count_extraverse += 1
    if x.index(i) in [3, 7, 12, 16, 20, 24, 28, 32, 36, 
            40, 44, 48, 56, 60, 64, 68, 72, 75, 79, 83, 86, 89,94, 98] and i[1] == ' +': 
        count_neyrotism += 1
    if x.index(i) in [4, 8, 17, 25, 29, 41, 45, 49, 65, 69, 76, 80, 82,91,93] and i[1] == ' -':
        count_sincerity += 1
    if x.index(i) in [13, 21, 33, 37, 61, 73, 87, 99] and i[1] == ' +':
        count_sincerity += 1

total = count_psychotism + count_extraverse + count_neyrotism + count_sincerity

print('Общий балл - ', total, '\n',
      'Психотизм - ', count_psychotism, ' баллов из 20!', '\n',
      'Экстраверсия-интроверсия - ', count_extraverse, ' баллов из 14!', '\n',
      'Нейротизм - ', count_neyrotism, ' баллов из 24!', '\n',
      'Искренность - ', count_sincerity, ' баллов из 23!', '\n',)