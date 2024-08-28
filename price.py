import pandas as pd

# Чтение CSV-файла
df = pd.read_csv('prices.csv')

# Предположим, что нужный столбец называется 'Цена'
# Удаляем '₽/мес.' и преобразуем данные в числа
df['Price'] = df['Price'].str.replace('₽/мес.', '').str.replace(' ', '').astype(float)

# Сохраняем изменения в новый CSV-файл, если это необходимо
df.to_csv('processed_file.csv', index=False)

# Печатаем обработанные данные
print(df)