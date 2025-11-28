import pandas as pd
pd.set_option('display.max_rows',None)
# a=pd.DataFrame(data=...,index=[0,1,2],columns=['q','w'], dtype=...)      #data самый главный, остальные необязательно
data=pd.read_csv('wine.csv')
""" 
print(data.head())

print(data.count()) #считает непустые ячейки по столбикам 

print(data.shape())

print(data.describe()) #числовые и статистические данные int/float 

print(data.isna().sum()) #покажет таблицу из булеанскик значение True//False//"пусто" + сумма пустых значений 

data.dropna(axis=0, how='any')  # 0 - удаление строк; 1 - удаление столбцов; any//all

print(data[['price','country','winery']].head())
print(data.price.head())

print(data[10:15]) #получаем все от 10 строки до 15 НЕ включительно
print(data.loc[10:15,['country','price']]) 

print(data[data['price']>300].price.head())
print(data[(data.price>300) & (data.country == 'US')][['price','country']])
"""



print(data[(data.price>300) & (data.country == 'US')].count()) 

print(data.groupby(['country','price']).count())




