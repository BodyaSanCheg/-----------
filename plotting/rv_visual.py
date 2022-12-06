from sre_parse import fix_flags
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Построение случайного блуждания
rw = RandomWalk(num_points = 50_000)
rw.fill_walk()

# Нанесение точек на диаграмму
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
point_number = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues,
    edgecolors='none', s=1)

# Выделение первой и последней точек
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100)

# Elfktybt jctq
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
