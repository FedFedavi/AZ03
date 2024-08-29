import numpy as np
import matplotlib.pyplot as plt


random_array1 = np.random.rand(5)
random_array2 = np.random.rand(5)
print(random_array1, random_array2)

plt.scatter(random_array1, random_array2)
# #
#
plt.xlabel('array1')
plt.ylabel('array2')
plt.title('Диаграмма рассеивания двух наборов')
# # plt.grid(True)
plt.show()