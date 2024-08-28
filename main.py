import matplotlib.pyplot as plt

# x = [2, 6, 8, 14, 20]
# y = [6, 4, 10, 12, 16]
#
# plt.plot(x, y)
# plt.title('Пример простого линейного графика')
# plt.xlabel('x ось')
# plt.ylabel('y ось')
#
# plt.show()
#
# data = [5, 6, 7, 4, 6, 5, 7, 8, 5, 8, 9, 10, 11, 8, 9, 10, 7, 6, 5, 7, 8, 9, 10, 7, 6, 5]
# plt.hist(data, bins=3)

x = [1, 4, 6, 7]
y = [3, 5, 8, 10]

plt.scatter(x, y)

plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('Тестовая диаграмма рассеивания')
plt.show()