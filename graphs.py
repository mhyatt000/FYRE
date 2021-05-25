import matplotlib.pyplot as plt
import numpy

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(132)
plt.bar(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
plt.show()
