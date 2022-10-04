import numpy as np
import csv
import statistics as st


data = []
inf = open('fns_for_model.csv','r') 
data = list(csv.reader(inf, delimiter=';')) #считывание файла и отдельное запоминание первой строки (названия)
names = [row[:] for row in data[0]]
inf.close()

del data[0]
data = np.array(data, dtype=float) #убираем названия, меняем тип на флот, транспорнируем
data = data.transpose()

for i in range(1, len(names)): #вывод ср знач и дисперсии 
    print('Mean and variance (', names[i],') =', st.mean(data[i]),', ', st.variance(data[i])) 

