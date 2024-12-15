import pandas as pd
import os

from shared import mem_usage, opt_obj, opt_int, opt_float, get_memory_stat_by_column

df = pd.read_csv('TMDB.csv')

# Задание 4
dataset_obj = df.select_dtypes(include=['object']).copy()
converted_obj = opt_obj(df)

print('Объем памяти колонок типа object: ', mem_usage(dataset_obj))
print('Объем памяти преобразованных колонок в тип Categorial: ', mem_usage(converted_obj))

# Задание 5
converted_int = opt_int(df)

# Задание 6
converted_float = opt_float(df)

# Задание 7
converted_df = pd.concat([converted_obj, converted_int, converted_float], axis=1)
print('Итого теперь колонки весят: ', mem_usage(converted_df))
print('Раньше весили: ', mem_usage(df))

memory_info = get_memory_stat_by_column(converted_df)
memory_df = pd.DataFrame(memory_info)
memory_df.to_csv('./outputs/memory_after_opt.csv')

converted_df.to_csv('TMDB_converted.csv')
file_memory_bytes = os.path.getsize('TMDB_converted.csv')
print('Объем памяти файла на диске: ', file_memory_bytes / 1024 / 1024, 'Мб')
