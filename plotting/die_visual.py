from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Создание двух кубиков D6
die1 = Die(num_sides=6)
die2 = Die(num_sides=10)


# Моделирование серии (times) бросков с сохранением результатов в списке
results = []
times = 50_000
for roll_num in range(times):
    result = die1.roll() + die2.roll()
    results.append(result)

# Анализ результатов
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axix_config = {'title': 'Result', 'dtick': 1}
y_axix_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling a D{die1.num_sides} and a D{die2.num_sides} dices {times} times',
        xaxis=x_axix_config, yaxis=y_axix_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d10.html')