import pandas as pd

# Параметры
file_path = 'TMDB.csv'
output_file_path = 'subset_data.csv'

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

subset_df = pd.DataFrame()

for chunk in pd.read_csv(file_path, usecols=columns_to_use, dtype=dtypes, chunksize=10000):
    subset_df = pd.concat([subset_df, chunk], ignore_index=True)

subset_df.to_csv(output_file_path, index=False)
