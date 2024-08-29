import pandas as pd

# Чтение данных из CSV файла
df = pd.read_csv('prices.csv')

# Удаление строк, содержащих только "руб."
df = df[df['Price'] != 'руб.']

# Преобразование цен в целые числа
df['Price'] = df['Price'].str.replace('руб.', '').str.replace(' ', '').astype(int)

# Сохранение обратно в CSV файл, если необходимо
df.to_csv('prices_cleaned.csv', index=False)

print(df)