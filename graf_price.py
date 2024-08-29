import pandas as pd
import matplotlib.pyplot as plt

# Чтение обработанного CSV-файла
df = pd.read_csv('prices_cleaned.csv')

# Предположим, что столбец с ценами называется 'Цена'
price = df['Price']

# Построение гистограммы
# plt.figure(figsize=(10, 6))  # Задаем размер фигуры
plt.hist(price, bins=10, edgecolor='black')  # Выбираем число корзин (bins)
plt.title('Распределение цен')
plt.xlabel('Цена (₽)')
plt.ylabel('Частота')
plt.grid(True)

# Отображение гистограммы
plt.show()