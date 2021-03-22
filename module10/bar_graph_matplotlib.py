import matplotlib.pyplot as plt

fig, ax = plt.subplots()

data = {
    "France": 65.4,
    "Germany": 82.4,
    "Italy": 59.2,
    "UK": 66.9
}

x_axis_data = data.keys()
y_axis_data = data.values()

ax.bar(x_axis_data, y_axis_data)

ax.set(ylim=[0, 100],
       ylabel='Population (in millions)',
       xlabel='Country',
       title='European Countries by Population')

plt.show()
