import pandas as pd

df = pd.read_csv('./Mall_Customers.csv', sep=',') 
average= df.groupby('Genre').mean()
print('средняя доходность женщин',average['Annual Income (k$)']['Female'])



df = pd.read_csv('./Mall_Customers.csv', sep=',') 
average=df.groupby('Genre').max()
print(average[['CustomerID','Annual Income (k$)']])


from matplotlib import pyplot as plt

plt.figure(figsize=(15, 4))
df = pd.read_csv('./Mall_Customers.csv', sep=',')
df = df.loc[df['Genre']== 'Male']
df = df.drop_duplicates(subset=['Annual Income (k$)'])
plt.scatter(df['Annual Income (k$)'].values,df['Age'].values)
plt.xlabel('Annual Income (k$)')
plt.ylabel('Age')
plt.show()


import seaborn as sns

df = pd.read_csv('./Mall_Customers.csv', sep=',')
sns.histplot(data=df, x='Annual Income (k$)', hue='Genre', weights='Spending Score (1-100)', multiple='dodge', palette={'Male': 'blue', 'Female': 'pink'})
plt.title('Распределение расходов в зависимости от доходов')
plt.xlabel('Годовой доход (k$)')
plt.ylabel('Общие расходы (оценка)')
plt.grid(axis='y')
plt.show()