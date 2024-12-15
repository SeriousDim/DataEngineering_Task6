import pandas as pd
import os
import json

from shared import get_memory_stat_by_column

# Задание 1-3
df = pd.read_csv('TMDB.csv')
memory_info = get_memory_stat_by_column(df)

file_memory_bytes = os.path.getsize('TMDB.csv')
print('Объем памяти файла на диске: ', file_memory_bytes / 1024 / 1024, 'Мб')

memory_usage_stat = df.memory_usage(deep=True)
total_memory_usage = memory_usage_stat.sum()
print('Объем памяти загруженного файла: ', total_memory_usage / 1024 / 1024, 'Мб')

memory_df = pd.DataFrame(memory_info)
memory_df.to_csv('./outputs/memory_before_opt.csv')

with open('./outputs/task3_before_opt.json', 'w', encoding='utf-8') as file:
    json.dump(memory_info, file, ensure_ascii=False, indent=4)
