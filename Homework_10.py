import pandas as pd
fruits= ["apple", "pear", "orange", "tangerine", "banana", "kiwi", "peach", "plum", "grape", "pineapple"]
fruits_series = pd.Series(fruits)
print(fruits_series)





import pandas as pd
df= pd.DataFrame({
    'fruits_1': ["apple", "pear", "orange", "tangerine", "banana"],
    'fruits_2': [ "tangerine", "banana", "kiwi", "peach", "plum"]})
print(df)
print( df[df != df.loc[df['fruits_1'].isin(df['fruits_2']), 'fruits_1'].values].dropna())




import pandas as pd
from matplotlib import pyplot as plt

sr= pd.Series(["orange","orange","orange","orange","orange", "tangerine", "banana", "tangerine", "banana", "tangerine", "banana", "tangerine", "tangerine", "tangerine", "tangerine"])
print(sr)

plt.bar(sr.value_counts().index, sr.value_counts().values)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()





import pandas as pd

df_fruits= pd.DataFrame({
    'fruits': ["apple", "pear", "orange", "tangerine", "banana"],
    'vegetables': [ "onion", "garlic", "beetroot", "carrot", "cabbage"]})
print('fruits')
print(df_fruits)
df_vegetables= pd.DataFrame({
    'vegetables': ["cucumber", "tomato", "zucchini", "eggplant", "potato"],
    'fruits': [ "tangerine", "banana", "kiwi", "peach", "plum"]})
print('vegetables')
print(df_vegetables)
df_berries= pd.DataFrame({
    'berries': [ "strawberry", "raspberry", "blueberry", "blueberry", "currant", "gooseberry", "cherry", "cherry", "grape", "watermelon"]})
df_berries.index.name = 'Number'
print('berries')
print(df_berries)
df_fruits_vegetables= pd.concat([df_fruits,df_vegetables]).reset_index(drop=True)
df_fruits_vegetables.index.name = 'Number'
print('fruits_vegetables')
print( df_fruits_vegetables)
df_fruits_vegetables_berries= pd.merge(df_fruits_vegetables,df_berries,how = "outer",on='Number')
print('fruits_vegetables_berries')
print(df_fruits_vegetables_berries)




from matplotlib import pyplot as plt
import pandas as pd

df_fruits_price = pd.DataFrame({
    'Banana':[0.34, 0.36, 0.35, 0.39, 0.36, 0.37, 0.38, 0.36, 0.42, 0.45, 0.46, 0.48, 0.46, 0.44, 0.46, 0.49, 0.49, 0.49, 0.49, 0.49, 0.5, 0.51, 0.51, 0.51, 0.5, 0.49, 0.5, 0.51, 0.61, 0.61, 0.58, 0.61, 0.6, 0.6, 0.6, 0.58, 0.57, 0.56],
    'Apple':[0.63, 0.57, 0.64, 0.59, 0.66, 0.68, 0.77, 0.73, 0.73, 0.69, 0.72, 0.89, 0.89, 0.83, 0.8, 0.83, 0.93, 0.91, 0.94, 0.9, 0.92, 0.87, 0.95, 0.98, 1.04, 0.95, 1.07, 1.12, 1.32, 1.18, 1.22, 1.35, 1.38, 1.39, 1.35, 1.36, 1.44, 1.29] 
}, index=[i for i in range(1980,2018)]) 
print(list(df_fruits_price['Banana']))

plt.plot(list(df_fruits_price.index),list(df_fruits_price['Banana']), label='Banana', color='green')
plt.plot(list(df_fruits_price.index),list(df_fruits_price['Apple']), label='Apple', color='red')
plt.xlabel('Год')
plt.ylabel('Средняя цена за фунт (453,6 г), $')
plt.legend()
plt.grid()
plt.show()