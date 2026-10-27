import matplotlib.pyplot as plt
import pandas as pd

chit = pd.read_parquet('titanic.parquet') #Читаем в виде паркета
chit.to_csv('titanic.csv') #переводим в тип csv
df = pd.read_csv('titanic.csv') #теперь читаем в виде csv 
a = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0) #Группируем по Классам и выживаемости
gist = a.div(a.sum(axis=1), axis=0) * 100 #Делаем проценты
gist.plot(kind='bar', stacked=True) #Строем гистограмму 

#Настройки для гистограммы

plt.title('Выживаемость пассажиров от класса') 
plt.xlabel('Класс') 
plt.ylabel('% выживаемости') 
plt.xticks(rotation=0)
plt.legend(['Не выжил', 'Выжил']) 
plt.tight_layout()
plt.show() #показ