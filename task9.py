import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

columns_to_use = ['vote_average', 'vote_count', 'status', 'revenue', 'runtime',
                  'adult', 'budget', 'genres', 'spoken_languages', 'keywords']
dtypes = {
    'vote_average': 'float32',
    'vote_count': 'uint16',
    'status': 'category',
    'revenue': 'uint32',
    'runtime': 'uint16',
    'adult': 'bool',
    'budget': 'uint32',
    'genres': 'category',
    'spoken_languages': 'category',
    'keywords': 'category'
}

df = pd.read_csv('subset_data.csv', usecols=columns_to_use, dtype=dtypes)

plt.figure(figsize=(8, 6))
df['adult'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('adult')
plt.savefig('./outputs/adult_pie.png')
plt.close()

budget = df[(df['budget'] < 3_000_000) & (df['budget'] > 0.0)]['budget']
plt.figure(figsize=(8, 6))
plt.hist(budget, bins=40, alpha=0.7, color='blue', edgecolor='black')
plt.title('budget')
plt.savefig('./outputs/budget_hist.png')
plt.close()

num_df = df.select_dtypes(include=['uint16', 'uint32', 'float']).copy()
plt.figure(figsize=(8, 6))
sns.heatmap(num_df.corr(), annot=True)
plt.savefig('./outputs/correlation.png')
plt.close()

plt.figure(figsize=(30, 6))
plt.plot(df['vote_count'], df['budget'], color='blue', label='vote_count от budget')
plt.title('Линейный график')
plt.xlabel('vote_count')
plt.ylabel('budget')
plt.legend()
plt.grid()
plt.savefig('./outputs/budget_vote_count_linear.png')
plt.close()

plt.figure(figsize=(30, 6))
plt.scatter(df['revenue'], df['budget'], color='blue', label='revenue от budget')
plt.title('Линейный график')
plt.xlabel('revenue')
plt.ylabel('budget')
plt.legend()
plt.grid()
plt.savefig('./outputs/budget_revenue_scatter.png')
plt.close()
